from ollama import Client

from config.settings import settings
from llm.base import BaseLLMProvider


class OllamaProvider(BaseLLMProvider):
    """
    Local Ollama implementation of the LLM provider.
    """

    def __init__(self) -> None:
        self.client = Client(host=settings.ollama_base_url)
        self.model = settings.ollama_model

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

            response = self.client.chat(
                model=self.model,
                messages=messages,
                options={
                    "temperature": settings.llm_temperature,
                },
            )

            return response["message"]["content"]

        except Exception as error:
            raise RuntimeError(
                f"Ollama provider failed. Make sure Ollama is running and model '{self.model}' is pulled. Error: {error}"
            ) from error