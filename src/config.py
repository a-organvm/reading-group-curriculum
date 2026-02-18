"""Settings from environment variables."""

import os


class Settings:
    """Application settings loaded from environment variables."""

    DATABASE_URL: str = os.environ.get("DATABASE_URL", "")

    @classmethod
    def require_db(cls) -> str:
        """Return DATABASE_URL or raise if unset. Converts to psycopg driver."""
        if not cls.DATABASE_URL:
            raise RuntimeError("DATABASE_URL is not set")
        url = cls.DATABASE_URL
        if url.startswith("postgresql://") and "+psycopg" not in url:
            url = url.replace("postgresql://", "postgresql+psycopg://", 1)
        return url
