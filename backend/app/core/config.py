from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    # Application
    api_env: str = "development"
    api_secret_key: str = "change_me_in_production"

    # Database
    postgres_user: str = "eckmatch"
    postgres_password: str = "eckmatch_dev"
    postgres_db: str = "eckmatch_db"
    postgres_host: str = "localhost"
    postgres_port: int = 5432

    @property
    def database_url(self) -> str:
        """Build the full PostgreSQL connection URL."""
        return (
            f"postgresql://{self.postgres_user}:{self.postgres_password}"
            f"@{self.postgres_host}:{self.postgres_port}/{self.postgres_db}"
        )

    model_config = {"env_file": ".env", "case_sensitive": False}


settings = Settings()
