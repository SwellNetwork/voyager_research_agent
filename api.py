from contextlib import asynccontextmanager

from fastapi import FastAPI

from src.agent.session_manager import SessionManager
from src.api.v1_router import v1_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    app.state.session_manager = SessionManager()
    yield


app = FastAPI(lifespan=lifespan)
app.include_router(v1_router)
if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8082, log_level="info")