from config.settings import settings
from llm.factory import get_llm_provider


SYSTEM_PROMPT = """
You are an AI Research Assistant Agent.
Explain answers clearly, accurately, and in a beginner-friendly way.
If you are unsure, say you are unsure instead of guessing.
"""


def main() -> None:
    print("=" * 60)
    print(settings.app_name)
    print(f"Environment: {settings.app_env}")
    print(f"Selected LLM Provider: {settings.llm_provider}")
    print("=" * 60)

    llm = get_llm_provider()

    print("Chatbot is ready. Type 'exit' to stop.")
    print()

    while True:
        user_message = input("You: ")

        if user_message.lower().strip() in ["exit", "quit"]:
            print("Assistant: Goodbye!")
            break

        if not user_message.strip():
            print("Assistant: Please enter a valid message.")
            continue

        try:
            print()
            print("Assistant:")
            
            for token in llm.stream_response(
                user_message=user_message,
                system_prompt=SYSTEM_PROMPT,
            ):
                print(token, end="", flush=True)

            print()
            print()

        except Exception as error:
            print()
            print(f"Error: {error}")
            print()


if __name__ == "__main__":
    main()