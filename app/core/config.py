from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    APP_NAME:str = "RGS"
    APP_ENV:str = "development"
    
    model_config = SettingsConfigDict(
        env_file =".env",
        env_file_encoding="utf-8",
        case_sensitive=True 
    )
    
settings = Settings()