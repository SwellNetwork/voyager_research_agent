import asyncio
import json
import re
import textwrap
from pathlib import Path

import streamlit as st
import streamlit.components.v1 as components

from src.agent.session_manager import SessionManager

REPORT_PATH = Path("resource/HYPE_analysis_with_charts.md")
SECTION_LIMIT = 11

def _iter_sse_payloads(sse_blob: str) -> list[dict]:
    payloads: list[dict] = []
    for line in sse_blob.splitlines():
        if not line.startswith("data:"):
            continue
        raw = line[len("data:"):].strip()
        if not raw:
            continue
        try:
            payloads.append(json.loads(raw))
        except json.JSONDecodeError:
            continue
    return payloads


def _run_stream(
    session_manager: SessionManager,
    session_id: str,
    query: str,
    placeholder: st.delta_generator.DeltaGenerator,
    context: str = "",
) -> str:
    state: dict[str, str | list[str]] = {"final": "", "parts": []}

    async def _stream() -> None:
        async for sse_blob in session_manager.stream_chat(query, session_id, context=context):
            for payload in _iter_sse_payloads(sse_blob):
                event_type = payload.get("type")
                content = payload.get("content", "")
                if event_type == "message_output_partial":
                    state["parts"].append(content)
                    placeholder.markdown("".join(state["parts"]))
                elif event_type == "message_output":
                    if content:
                        state["final"] = content
                        placeholder.markdown(content)

    asyncio.run(_stream())
    return state["final"] or "".join(state["parts"])


def _trim_sidebar_text(text: str, width: int = 60) -> str:
    cleaned = " ".join(text.split())
    if not cleaned:
        return ""
    return textwrap.shorten(cleaned, width=width, placeholder="...")

def _stringify_content(content: object) -> str:
    if isinstance(content, str):
        return content
    if isinstance(content, list):
        parts: list[str] = []
        for part in content:
            if isinstance(part, str):
                parts.append(part)
            elif isinstance(part, dict):
                text = part.get("text")
                if isinstance(text, str):
                    parts.append(text)
        return "\n\n".join([p for p in parts if p.strip()])
    if isinstance(content, dict):
        text = content.get("text")
        if isinstance(text, str):
            return text
    return ""


def _normalize_loaded_messages(items: list[dict]) -> list[dict]:
    messages: list[dict] = []
    for item in items:
        role = item.get("role")
        if role not in {"user", "assistant"}:
            continue
        content = _stringify_content(item.get("content"))
        messages.append({"role": role, "content": content})
    return messages


def _load_session_conversation(session_id: str) -> None:
    session_manager = st.session_state.session_manager
    if session_id not in session_manager.sessions:
        asyncio.run(session_manager.create_session(session_id))
    items = asyncio.run(session_manager._load_conversation(session_id, True))
    st.session_state.active_session_id = session_id
    st.session_state.messages = _normalize_loaded_messages(items)

def _parse_report_sections(path: Path) -> list[dict]:
    md_text = path.read_text(encoding="utf-8").replace("](charts/", "](resource/charts/")
    lines = md_text.splitlines()
    sections: list[dict] = []
    preface_blocks: list[dict] = []
    current: dict | None = None
    buffer: list[str] = []

    section_pattern = re.compile(r"^##\s+(?P<title>.+)$")
    numbered_section_pattern = re.compile(r"^\d+\.\s+")
    image_pattern = re.compile(r"!\[(?P<alt>.*?)]\((?P<src>[^)]+)\)")
    link_pattern = re.compile(r"\[(?P<label>Interactive.*?)]\((?P<href>[^)]+)\)")

    def target_blocks() -> list[dict]:
        return current["blocks"] if current is not None else preface_blocks

    def flush_buffer() -> None:
        if buffer:
            target_blocks().append({"type": "markdown", "content": "\n".join(buffer)})
            buffer.clear()

    for line in lines:
        section_match = section_pattern.match(line)
        if section_match:
            title = section_match.group("title").strip()
            if numbered_section_pattern.match(title) and len(sections) < SECTION_LIMIT:
                flush_buffer()
                current = {"title": title, "blocks": []}
                sections.append(current)
                if preface_blocks:
                    current["blocks"].extend(preface_blocks)
                    preface_blocks.clear()
                continue

        image_match = image_pattern.fullmatch(line.strip())
        if image_match:
            flush_buffer()
            alt = image_match.group("alt")
            src = image_match.group("src")
            target_blocks().append({"type": "image", "src": src, "alt": alt})
            continue

        link_match = link_pattern.fullmatch(line.strip())
        if link_match:
            href = link_match.group("href")
            if href.endswith(".html") and Path(href).exists():
                png_path = Path(href).with_suffix(".png")
                if png_path.exists():
                    continue
                flush_buffer()
                target_blocks().append({"type": "html", "src": href})
            else:
                buffer.append(line)
            continue

        buffer.append(line)

    flush_buffer()

    if not sections:
        sections.append({"title": "Report", "blocks": preface_blocks})
    elif preface_blocks:
        sections[0]["blocks"] = preface_blocks + sections[0]["blocks"]

    return sections[:SECTION_LIMIT]


def _get_report_sections(path: Path) -> list[dict]:
    mtime = path.stat().st_mtime if path.exists() else None
    cached_mtime = st.session_state.get("report_sections_mtime")
    cached_sections = st.session_state.get("report_sections")
    if mtime is not None and cached_sections is not None and cached_mtime == mtime:
        return cached_sections

    if not path.exists():
        return []

    sections = _parse_report_sections(path)
    st.session_state.report_sections = sections
    st.session_state.report_sections_mtime = mtime
    return sections


def _render_report_sections(sections: list[dict]) -> None:
    if not sections:
        st.info("Report is empty or could not be parsed.")
        return

    def section_to_text(section: dict) -> str:
        lines: list[str] = [f"# {section.get('title', 'Report Section')}"]
        for block in section.get("blocks", []):
            block_type = block.get("type")
            if block_type == "markdown":
                content = block.get("content", "")
                if content:
                    lines.append(content)
            elif block_type == "image":
                alt = block.get("alt") or "chart"
                src = block.get("src", "")
                lines.append(f"[image] {alt}: {src}")
            elif block_type == "html":
                src = block.get("src", "")
                lines.append(f"[interactive] {src}")
        return "\n\n".join(lines).strip()

    for index, section in enumerate(sections):
        title = section.get("title", f"Section {index + 1}")
        with st.expander(title, expanded=(index == 0)):
            if st.button(
                "Analyze with Agent",
                key=f"analyze-section-{index}",
                use_container_width=True,
            ):
                st.session_state.context_by_session[
                    st.session_state.active_session_id
                ] = section_to_text(section)
                st.rerun()
            for block in section.get("blocks", []):
                block_type = block.get("type")
                if block_type == "markdown":
                    st.markdown(block.get("content", ""))
                elif block_type == "image":
                    st.image(block.get("src", ""), caption=block.get("alt") or None)
                elif block_type == "html":
                    html_path = Path(block.get("src", ""))
                    if html_path.exists():
                        html = html_path.read_text(encoding="utf-8")
                        components.html(html, height=420, scrolling=True)


def run() -> None:
    st.set_page_config(page_title="Voyager Research Agent", page_icon="🧭", layout="wide")
    st.title("Voyager Research Agent")

    if "messages" not in st.session_state:
        st.session_state.messages = []
    if "session_manager" not in st.session_state:
        st.session_state.session_manager = SessionManager()
    if "active_session_id" not in st.session_state:
        st.session_state.active_session_id = asyncio.run(
            st.session_state.session_manager.create_session()
        )
    if "context_by_session" not in st.session_state:
        st.session_state.context_by_session = {}
    st.markdown(
        """
        <style>
        .st-key-chat-panel {
            display: flex;
            flex-direction: column;
            height: calc(100vh - 220px);
        }
        .st-key-history-panel {
            height: calc(100vh - 220px);
            overflow-y: auto;
            padding-right: 0.5rem;
        }
        .st-key-report-panel {
            height: calc(100vh - 220px);
            overflow-y: auto;
            padding-right: 0.5rem;
        }
        .st-key-chat-messages {
            flex: 1 1 auto;
            overflow-y: auto;
            padding-right: 0.5rem;
        }
        .st-key-chat-input {
            margin-top: auto;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )

    chat_tab, report_tab = st.tabs(["Chat Agent", "Report"])

    with chat_tab:
        history_col, chat_col = st.columns([1, 2], gap="large")

        with history_col:
            history_panel = st.container(key="history-panel")
            with history_panel:
                header_cols = st.columns([3, 1])
                with header_cols[0]:
                    st.subheader("Chat History")
                with header_cols[1]:
                    if st.button("🆕", key="new-session", use_container_width=True, help="New chat"):
                        new_session_id = asyncio.run(
                            st.session_state.session_manager.create_session()
                        )
                        st.session_state.active_session_id = new_session_id
                        st.session_state.messages = []
                session_ids = st.session_state.session_manager.session_ids or list(
                    st.session_state.session_manager.sessions.keys()
                )
                if session_ids:
                    for session_id in session_ids:
                        preview = st.session_state.session_manager.get_session_preview(session_id)
                        if not preview:
                            continue
                        label = _trim_sidebar_text(preview)
                        if session_id == st.session_state.active_session_id:
                            label = f"▶ {label}"
                        if st.button(label, key=f"session-{session_id}"):
                            _load_session_conversation(session_id)
                else:
                    st.caption("No sessions yet.")

        with chat_col:
            chat_panel = st.container(key="chat-panel")
            with chat_panel:
                chat_container = st.container(key="chat-messages")
                with chat_container:
                    context_text = st.session_state.context_by_session.get(
                        st.session_state.active_session_id
                    )
                    if context_text:
                        with st.chat_message("assistant", avatar=":material/info:"):
                            st.markdown("**Context**")
                            with st.expander("Show context"):
                                st.markdown(context_text)
                    for message in st.session_state.messages:
                        st.chat_message(message["role"]).markdown(message["content"])

                with st.container(key="chat-input"):
                    prompt = st.chat_input("Ask a question", key="chat_input")
                    if prompt:
                        st.session_state.messages.append({"role": "user", "content": prompt})
                        context_text = st.session_state.context_by_session.get(
                            st.session_state.active_session_id, ""
                        )
                        with chat_container:
                            st.chat_message("user").markdown(prompt)

                            with st.chat_message("assistant"):
                                assistant_placeholder = st.empty()
                                response_text = _run_stream(
                                    st.session_state.session_manager,
                                    st.session_state.active_session_id,
                                    prompt,
                                    assistant_placeholder,
                                    context=context_text,
                                )

                        st.session_state.messages.append(
                            {"role": "assistant", "content": response_text}
                        )

    with report_tab:
        report_container = st.container(key="report-panel")
        with report_container:
            report_path = REPORT_PATH
            if report_path.exists():
                sections = _get_report_sections(report_path)
                _render_report_sections(sections)
            else:
                st.warning(f"Report not found at {REPORT_PATH}")
