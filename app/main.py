from config.settings import settings

def main() -> None:
    print("Application started successfully!")
    print(f"App Name: {settings.app_name}")
    print(f"App Environment: {settings.app_env}")

    if settings.openai_api_key and settings.openai_api_key != "your_api_key_here":
        print("Open API key loaded successfully! ")
    else: 
        print("Open API key not configured yet!")


if __name__ == "__main__":
    main()