import json
import os
import re
import textwrap
import uuid
from pathlib import Path
from urllib import error as urlerror
from urllib import request as urlrequest

import streamlit as st
import streamlit.components.v1 as components

REPORT_PATH = Path("resource/HYPE_analysis_with_charts.md")
SECTION_LIMIT = 11
API_BASE_URL = os.getenv("API_BASE_URL", "http://localhost:8082").rstrip("/")
CHAT_ENDPOINT = f"{API_BASE_URL}/v1/chat"
REQUEST_TIMEOUT_SECONDS = float(os.getenv("API_TIMEOUT_SECONDS", "600"))

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


def _new_session_id() -> str:
    return f"sess_{uuid.uuid4().hex}"


def _stream_chat_api(session_id: str, query: str, context: str = ""):
    payload = {
        "query": query,
        "session_id": session_id,
        "context": context,
    }
    data = json.dumps(payload).encode("utf-8")
    request = urlrequest.Request(
        CHAT_ENDPOINT,
        data=data,
        headers={
            "Content-Type": "application/json",
            "Accept": "text/event-stream",
        },
        method="POST",
    )
    with urlrequest.urlopen(request, timeout=REQUEST_TIMEOUT_SECONDS) as response:
        for raw_line in response:
            if not raw_line:
                continue
            yield raw_line.decode("utf-8", errors="ignore")


def _run_stream(
    session_id: str,
    query: str,
    placeholder: st.delta_generator.DeltaGenerator,
    context: str = "",
) -> str:
    state: dict[str, str | list[str]] = {"final": "", "parts": []}
    try:
        for sse_blob in _stream_chat_api(session_id, query, context=context):
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
    except urlerror.HTTPError as exc:
        placeholder.markdown(f"Chat API error (HTTP {exc.code}).")
    except urlerror.URLError as exc:
        placeholder.markdown(f"Could not reach chat API. {exc.reason}")
    except Exception as exc:
        placeholder.markdown(f"Chat API failed. {exc}")

    return state["final"] or "".join(state["parts"])


def _trim_sidebar_text(text: str, width: int = 60) -> str:
    cleaned = " ".join(text.split())
    if not cleaned:
        return ""
    return textwrap.shorten(cleaned, width=width, placeholder="...")

def _get_session_preview(session_id: str) -> str:
    messages = st.session_state.messages_by_session.get(session_id, [])
    for message in reversed(messages):
        content = message.get("content", "")
        if isinstance(content, str) and content.strip():
            return content
    return ""


def _load_session_conversation(session_id: str) -> None:
    st.session_state.active_session_id = session_id
    st.session_state.messages_by_session.setdefault(session_id, [])

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

    if "messages_by_session" not in st.session_state:
        st.session_state.messages_by_session = {}
    if "session_ids" not in st.session_state:
        st.session_state.session_ids = []
    if "active_session_id" not in st.session_state:
        new_session_id = _new_session_id()
        st.session_state.active_session_id = new_session_id
        st.session_state.session_ids.insert(0, new_session_id)
        st.session_state.messages_by_session[new_session_id] = []
    if "context_by_session" not in st.session_state:
        st.session_state.context_by_session = {}
    if st.session_state.active_session_id not in st.session_state.session_ids:
        st.session_state.session_ids.insert(0, st.session_state.active_session_id)
    st.session_state.messages_by_session.setdefault(st.session_state.active_session_id, [])
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
                        new_session_id = _new_session_id()
                        st.session_state.active_session_id = new_session_id
                        st.session_state.messages_by_session[new_session_id] = []
                        st.session_state.session_ids.insert(0, new_session_id)
                session_ids = st.session_state.session_ids or list(
                    st.session_state.messages_by_session.keys()
                )
                if session_ids:
                    for session_id in session_ids:
                        preview = _get_session_preview(session_id)
                        label = _trim_sidebar_text(preview) if preview else "New session"
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
                    messages = st.session_state.messages_by_session.get(
                        st.session_state.active_session_id, []
                    )
                    for message in messages:
                        st.chat_message(message["role"]).markdown(message["content"])

                with st.container(key="chat-input"):
                    prompt = st.chat_input("Ask a question", key="chat_input")
                    if prompt:
                        messages = st.session_state.messages_by_session.setdefault(
                            st.session_state.active_session_id, []
                        )
                        messages.append({"role": "user", "content": prompt})
                        context_text = st.session_state.context_by_session.get(
                            st.session_state.active_session_id, ""
                        )
                        with chat_container:
                            st.chat_message("user").markdown(prompt)

                            with st.chat_message("assistant"):
                                assistant_placeholder = st.empty()
                                response_text = _run_stream(
                                    st.session_state.active_session_id,
                                    prompt,
                                    assistant_placeholder,
                                    context=context_text,
                                )

                        messages.append({"role": "assistant", "content": response_text})

    with report_tab:
        report_container = st.container(key="report-panel")
        with report_container:
            report_path = REPORT_PATH
            if report_path.exists():
                sections = _get_report_sections(report_path)
                _render_report_sections(sections)
            else:
                st.warning(f"Report not found at {REPORT_PATH}")
