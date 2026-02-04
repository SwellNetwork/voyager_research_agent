# Voyager Research Agent

A voyager research agent with:
- a FastAPI backend that exposes the agent over HTTP
- a Streamlit frontend UI that calls the API for chat

## Install

Install dependencies with uv:

```bash
uv sync
```

## Configure

Add your OpenAI API key to `.env`:

```bash
OPENAI_API_KEY=your_api_key_here
```

## How the app works

1. **API layer (`api.py`, `src/api/v1_router.py`)**
   - Starts a FastAPI app.
   - Exposes `POST /v1/chat` (SSE streaming response) and `GET /v1/health`.
   - Uses a shared `SessionManager` stored in `app.state`.

2. **Agent execution (`src/agent/executor.py`)**
   - Builds the OpenAI agent (model, instructions, tools).
   - Streams token/events from the agent and formats them as SSE payloads.
   - Supports optional context injection before running the query.

3. **UI layer (`src/app/streamlit_app.py`)**
   - Renders chat + report tabs in Streamlit.
   - Sends chat requests to `POST /v1/chat`.
   - Reads SSE events and progressively renders assistant output.
   - Stores per-session chat history in Streamlit state.

## Run

Start the API:

```bash
uv run uvicorn api:app --host 0.0.0.0 --port 8082 --reload
```

Then start the Streamlit app (in another terminal):

```bash
API_BASE_URL=http://localhost:8082 uv run streamlit run main.py
```
