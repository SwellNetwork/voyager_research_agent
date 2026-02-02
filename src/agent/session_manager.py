import asyncio
import json
import sqlite3
from pathlib import Path

import dotenv
from src.agent.executor import Executor
from agents import SQLiteSession
import uuid
from typing import Any

dotenv.load_dotenv()


class SessionManager:
    def __init__(self):
        self.db_path = "db/sessions.db"
        self.session_ids = self._load_session_ids()
        self.sessions = {session_id: SQLiteSession(session_id, self.db_path) for session_id in self.session_ids}

    async def create_session(self, session_id: str = None):
        if session_id is None:
            session_id = f"sess_{uuid.uuid4().hex}"
        self.sessions[session_id] = SQLiteSession(session_id, self.db_path)
        if session_id not in self.session_ids:
            self.session_ids.insert(0, session_id)
        return session_id

    async def stream_chat(self, query: str, session_id: str = None, context: str = ""):
        if not session_id or session_id not in self.sessions:
            session_id = await self.create_session(session_id)
        
        session = self.sessions[session_id]

        executor = Executor()

        async for event in executor.run_streamed(query, session, context):
            yield event

    def get_session_preview(self, session_id: str) -> str | None:
        db_path = Path(self.db_path)
        if not db_path.exists():
            return None

        try:
            conn = sqlite3.connect(str(db_path), check_same_thread=False)
        except sqlite3.Error:
            return None

        try:
            cursor = conn.execute(
                """
                SELECT message_data
                FROM agent_messages
                WHERE session_id = ?
                ORDER BY id DESC
                LIMIT 1
                """,
                (session_id,),
            )
            row = cursor.fetchone()
            if not row:
                return None
            return self._extract_preview_text(row[0])
        except sqlite3.Error:
            return None
        finally:
            conn.close()

    def _extract_preview_text(self, message_data: str) -> str | None:
        try:
            item = json.loads(message_data)
        except json.JSONDecodeError:
            return None
        return self._item_to_text(item)

    def _item_to_text(self, item: Any) -> str | None:
        if isinstance(item, str):
            return item
        if not isinstance(item, dict):
            return None

        if isinstance(item.get("text"), str):
            return item.get("text")

        content = item.get("content")
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
                    else:
                        nested = part.get("content")
                        if isinstance(nested, str):
                            parts.append(nested)
            if parts:
                return " ".join(parts)

        return None


    def _load_session_ids(self):
        # load session ids from db/sessions.db
        db_path = Path(self.db_path)
        if not db_path.exists():
            return []

        try:
            conn = sqlite3.connect(str(db_path), check_same_thread=False)
        except sqlite3.Error:
            return []

        try:
            cursor = conn.execute(
                """
                SELECT session_id
                FROM agent_sessions
                ORDER BY updated_at DESC
                """
            )
            rows = cursor.fetchall()
            return [row[0] for row in rows]
        except sqlite3.Error:
            return []
        finally:
            conn.close()

    async def _load_conversation(self, session_id: str, reformat: bool = False):
        session = SQLiteSession(session_id, self.db_path)
        items = await session.get_items()
        if reformat:
            items = await self._reformat_conversation(items)
        return items

    async def _reformat_conversation(self, items: list[dict[str, Any]]):
        results = []
        for item in items:
            if item.get("role") == "user":
                result = {
                    "role": "user",
                    "content": item.get("content"),
                }
            elif item.get("role") == "assistant":
                result = {
                    "role": "assistant",
                    "id": item.get("id"),
                    "content": [x.get("text") for x in item.get("content")],
                }
            elif item.get("role") is None:
                result = item
            results.append(result)
        return results
