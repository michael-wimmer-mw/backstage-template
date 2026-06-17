from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

    service_name: str = "${{ values.name }}"
    log_level: str = "INFO"
{%- if values.includeDatabase %}
    database_url: str = "postgresql+asyncpg://user:pass@localhost:5432/${{ values.name }}"
{%- endif %}


settings = Settings()