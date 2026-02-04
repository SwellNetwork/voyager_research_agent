from agents import Agent, ModelSettings, Runner, ItemHelpers, Session
from openai.types.shared import Reasoning, ReasoningEffort
from openai.types.responses import ResponseTextDeltaEvent
from typing_extensions import Literal
import json
from typing import Any
import dotenv
from src.agent.prompt import CONTEXT_TEMPLATE
from src.agent.instruction import INSTRUCTION_HYPE
from src.agent.tools.get_report_data import get_report_data

dotenv.load_dotenv()


def format_sse(payload: dict[str, Any]) -> str:
    return f"data: {json.dumps(payload)}\n"


class Executor:
    def __init__(self, model: str = "gpt-5.1"):
        self.agent = self._create_agent(
            model=model,
            instructions=INSTRUCTION_HYPE
        )
        self.result = None

    async def run(self, items: list[dict[str, Any]]):
        self.result = await Runner.run(self.agent, items)
        return self.result

    async def run_streamed(self, query: str, session: Session, context: str = ""):
        if len(context) > 0:
            query = CONTEXT_TEMPLATE.format(context=context, question=query)
            print("chat with context: ")
            print(context[:200])
        result = Runner.run_streamed(self.agent, query, session=session)
        async for event in result.stream_events():
            async for payload in self._yield_events(event):
                yield payload
        self.result = result

    def _create_agent(
        self,
        name: str = "voyager-research-agent",
        model: str = "gpt-5.1", 
        reasoning_effort: ReasoningEffort = "medium",
        verbosity: Literal["low", "medium", "high"] | None = None,
        instructions: str = INSTRUCTION_HYPE,
    ):
        model_settings=ModelSettings(
            reasoning=Reasoning(
                effort=reasoning_effort), 
            verbosity=verbosity
        )
        tools = [
            get_report_data,
        ]
        agent = Agent(
            name=name,
            model=model,
            model_settings=model_settings,
            instructions=instructions,
            tools=tools,
        )
        return agent

    async def _yield_events(self, event):
        if event.type == "raw_response_event": # lv1
            if isinstance(event.data, ResponseTextDeltaEvent):
                yield format_sse({
                    "type": "message_output_partial",
                    "content": event.data.delta,
                })

        elif event.type == "agent_updated_stream_event": 
            yield format_sse({
                "type": "agent_updated",
                "content": event.new_agent.name,
            })
        elif event.type == "run_item_stream_event": # lv1
            if event.item.type == "message_output_item": # lv2
                yield format_sse({
                    "type": "message_output",
                    "content": ItemHelpers.text_message_output(event.item),
                })
