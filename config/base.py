from pydantic import Field, PostgresDsn, RedisDsn
from pydantic_settings import BaseSettings, SettingsConfigDict


class Config(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env", env_file_encoding="utf-8", extra="ignore"
    )
    in_debug: bool = Field(False, validation_alias="IN_DEBUG")
    host: str = Field("0.0.0.0", validation_alias="BIND_HOST")
    port: int = Field(8080, validation_alias="PORT")
    async_db_url: PostgresDsn = Field(
        "postgresql+asyncpg://username:password@127.0.0.1:5432/db_name",
        validation_alias="ASYNC_DB_URL",
    )
    sync_db_url: PostgresDsn = Field(
        "postgresql://username:password@127.0.0.1:5432/db_name",
        validation_alias="SYNC_DB_URL",
    )
    redis_url: RedisDsn = Field("rediss://:pass@localhost", validation_alias="REDIS_URL")
