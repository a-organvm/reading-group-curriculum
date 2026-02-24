"""Settings from environment variables."""

import os

from koinonia_db.config import require_database_url


class Settings:
    """Application settings loaded from environment variables."""

    DATABASE_URL: str = os.environ.get("DATABASE_URL", "")

    @classmethod
    def require_db(cls) -> str:
        """Return DATABASE_URL or raise if unset. Converts to psycopg driver."""
        return require_database_url()
