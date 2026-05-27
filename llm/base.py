from abc import ABC,abstractmethod
from email.generator import Generator

class BaseLLMProvider(ABC):
    """
        Common interface for all LLM providers.

        Any LLM provider such as OpenAI, Ollama, Claude, Gemini, or Azure OpenAI
        should follow this structure.
    """
    @abstractmethod
    def generate_response(self, user_message: str, system_prompt: str | None = None) -> str:
        """
        Generate a response from the selected LLM.

        Args:
            user_message: The user's question or instruction.
            system_prompt: Optional instruction that controls assistant behavior.

        Returns:
            The LLM-generated response as plain text.
        """
        pass
    @abstractmethod
    def stream_response(self, user_message: str, system_prompt: str | None = None,) -> Generator[str, None, None]:
        pass