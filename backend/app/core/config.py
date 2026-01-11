"""Application configuration settings."""

from typing import List, Optional

from pydantic import AnyHttpUrl, Field, field_validator
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """Application settings."""

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=True,
        extra="allow",
    )

    # Application
    APP_NAME: str = "Market Intelligence Platform"
    APP_ENV: str = "development"
    DEBUG: bool = True
    API_VERSION: str = "v1"
    SECRET_KEY: str = Field(..., min_length=32)

    # Server
    HOST: str = "0.0.0.0"
    PORT: int = 8000
    WORKERS: int = 4

    # CORS
    BACKEND_CORS_ORIGINS: List[AnyHttpUrl] = []

    @field_validator("BACKEND_CORS_ORIGINS", mode="before")
    @classmethod
    def assemble_cors_origins(cls, v: str | List[str]) -> List[str] | str:
        """Parse CORS origins."""
        if isinstance(v, str) and not v.startswith("["):
            return [i.strip() for i in v.split(",")]
        elif isinstance(v, (list, str)):
            return v
        raise ValueError(v)

    # Database
    DATABASE_URL: str
    DATABASE_POOL_SIZE: int = 20
    DATABASE_MAX_OVERFLOW: int = 10

    # Redis
    REDIS_URL: str

    # Vector Database - Pinecone
    PINECONE_API_KEY: Optional[str] = None
    PINECONE_ENVIRONMENT: Optional[str] = None
    PINECONE_INDEX_NAME: str = "market-intelligence"

    # Vector Database - Weaviate
    WEAVIATE_URL: Optional[str] = None
    WEAVIATE_API_KEY: Optional[str] = None

    # YouTube API
    YOUTUBE_API_KEY: str
    YOUTUBE_API_SERVICE_NAME: str = "youtube"
    YOUTUBE_API_VERSION: str = "v3"

    # Reddit API
    REDDIT_CLIENT_ID: str
    REDDIT_CLIENT_SECRET: str
    REDDIT_USER_AGENT: str = "MarketIntelligence/0.1.0"

    # OpenAI
    OPENAI_API_KEY: str
    OPENAI_MODEL: str = "gpt-4-turbo-preview"
    OPENAI_EMBEDDING_MODEL: str = "text-embedding-3-small"

    # Anthropic
    ANTHROPIC_API_KEY: Optional[str] = None
    ANTHROPIC_MODEL: str = "claude-3-sonnet-20240229"

    # Celery
    CELERY_BROKER_URL: str
    CELERY_RESULT_BACKEND: str

    # Authentication
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30
    REFRESH_TOKEN_EXPIRE_MINUTES: int = 10080
    ALGORITHM: str = "HS256"

    # Rate Limiting
    RATE_LIMIT_PER_MINUTE: int = 60

    # Monitoring
    SENTRY_DSN: Optional[str] = None

    # Logging
    LOG_LEVEL: str = "INFO"
    LOG_FORMAT: str = "json"

    # Feature Flags
    ENABLE_YOUTUBE: bool = True
    ENABLE_REDDIT: bool = True
    ENABLE_CACHING: bool = True

    # Limits (MVP)
    MAX_VIDEOS_PER_PROJECT: int = 100
    MAX_REDDIT_POSTS_PER_PROJECT: int = 500
    MAX_PROJECTS_FREE_TIER: int = 1
    MAX_PROJECTS_PRO_TIER: int = 10
    MAX_PROJECTS_AGENCY_TIER: int = 50


settings = Settings()
