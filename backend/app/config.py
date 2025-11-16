import os
from typing import Optional
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    """Application settings from environment variables"""
    
    # Server
    backend_host: str = os.getenv("BACKEND_HOST", "0.0.0.0")
    backend_port: int = int(os.getenv("BACKEND_PORT", "8000"))
    debug: bool = os.getenv("DEBUG", "False").lower() == "true"
    
    # Security
    api_key: str = os.getenv("API_KEY", "default-api-key-change-in-production")
    jwt_secret: str = os.getenv("JWT_SECRET", "your-jwt-secret-change-in-production")
    
    # AI Service - Gemini
    ai_provider: str = os.getenv("AI_PROVIDER", "gemini")
    gemini_api_key: str = os.getenv("GEMINI_API_KEY", "")
    gemini_model: str = os.getenv("GEMINI_MODEL", "gemini-pro")
    
    # Telegram Bot
    telegram_bot_token: str = os.getenv("TELEGRAM_BOT_TOKEN", "")
    telegram_bot_username: str = os.getenv("TELEGRAM_BOT_USERNAME", "")
    
    # Bot Service
    bot_host: str = os.getenv("BOT_HOST", "bot")
    bot_port: int = int(os.getenv("BOT_PORT", "5000"))
    bot_secret_key: str = os.getenv("BOT_SECRET_KEY", "default-bot-secret")
    
    # Frontend
    frontend_url: str = os.getenv("FRONTEND_URL", "http://localhost:3000")
    frontend_port: int = int(os.getenv("FRONTEND_PORT", "3000"))
    
    # CORS
    cors_origins: list = ["http://localhost:3000", "http://localhost:8000"]
    
    class Config:
        env_file = ".env"
        case_sensitive = False


settings = Settings()
