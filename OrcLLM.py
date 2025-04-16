import random
from typing import Optional, Any

from langchain_core.callbacks import CallbackManagerForLLMRun
from langchain_core.language_models import BaseChatModel
from langchain_core.messages import BaseMessage, AIMessage
from langchain_core.outputs import ChatResult, ChatGeneration


class OrcLLM(BaseChatModel):
    def _generate(self, messages: list[BaseMessage], stop: Optional[list[str]] = None,
                  run_manager: Optional[CallbackManagerForLLMRun] = None, **kwargs: Any) -> ChatResult:
        random_responses = [
            "Hello! How can I assist you today?",
            "This is a random message from OrcLLM.",
            "I'm here to help with any questions you have!",
            "OrcLLM at your service—what do you need?",
            "Here's something random for you to think about.",
        ]

        # Pick a random response
        random_message = random.choice(random_responses)

        # Handle stop tokens
        if stop:
            for stop_token in stop:
                if stop_token in random_message:
                    random_message = random_message.split(stop_token)[0]
                    break

        # Return the ChatResult containing the random message as a generation
        return ChatResult(
            generations=[ChatGeneration(message=AIMessage(content=random_message))]
        )

    @property
    def _llm_type(self) -> str:
        return "orc-gpt-1o"
