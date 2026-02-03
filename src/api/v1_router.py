from fastapi import APIRouter, HTTPException, Request
from fastapi.responses import StreamingResponse
from pydantic import BaseModel


v1_router = APIRouter(prefix="/v1")


class ChatRequest(BaseModel):
    query: str
    session_id: str | None = None
    context: str = ""


@v1_router.get("/health")
async def health() -> dict[str, str]:
    return {"status": "ok"}


@v1_router.post("/chat")
async def chat(payload: ChatRequest, request: Request) -> StreamingResponse:
    session_manager = getattr(request.app.state, "session_manager", None)
    if session_manager is None:
        raise HTTPException(status_code=500, detail="Session manager not initialized")

    async def event_generator():
        async for event in session_manager.stream_chat(
            query=payload.query,
            session_id=payload.session_id,
            context=payload.context,
        ):
            yield event

    headers = {
        "Cache-Control": "no-cache",
        "Connection": "keep-alive",
    }
    return StreamingResponse(
        event_generator(),
        media_type="text/event-stream",
        headers=headers,
    )
