from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    secret_key: str
    algorithm: str
    access_token_expire_minutes: int = 30
    database_name: str
    database_username: str
    database_password: str
    port: str
    host: str
    
    class Config:
        env_file = '.env'
        case_sensitive = False

settings = Settings()
