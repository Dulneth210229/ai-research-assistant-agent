from openai import OpenAI

from config.settings import settings
from llm.base import BaseLLMProvider


class OpenAIProvider(BaseLLMProvider):
    """
    OpenAI API implementation of the LLM provider.
    """

    def __init__(self) -> None:
        if not settings.openai_api_key or settings.openai_api_key == "your_openai_api_key_here":
            raise ValueError(
                "OpenAI API key is missing. Please set OPENAI_API_KEY in your .env file."
            )

        self.client = OpenAI(api_key=settings.openai_api_key)
        self.model = settings.openai_model

    def generate_response(self, user_message: str, system_prompt: str | None = None) -> str:
        try:
            messages = []

            if system_prompt:
                messages.append(
                    {
                        "role": "system",
                        "content": system_prompt,
                    }
                )

            messages.append(
                {
                    "role": "user",
                    "content": user_message,
                }
            )

            response = self.client.chat.completions.create(
                model=self.model,
                messages=messages,
                temperature=settings.llm_temperature,
            )

            return response.choices[0].message.content or ""

        except Exception as error:
            raise RuntimeError(f"OpenAI provider failed: {error}") from error