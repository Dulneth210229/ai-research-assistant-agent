from pydantic import BaseModel
from dotenv import load_dotenv
import os

load_dotenv()

class Settings(BaseModel):
    app_name: str = os.getenv("APP_NAME", "AI Research Assistant Agent")
    app_env: str = os.getenv("APP_ENV", "development")
    openai_api_key: str | None = os.getenv("OPENAI_API_KEY")


settings = Settings()