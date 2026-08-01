from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    PROJECT_NAME: str = "AstraQuant"
    VERSION: str = "1.0.0"
    ENVIRONMENT: str = "development"


settings = Settings()