from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    database_url: str
    storage_dir_root: str
    jwt_secret_key: str

    model_config = SettingsConfigDict(
        env_file=".env", # nơi lấy giá trị biến => chỉ cần viết thường lại tên trong .env
        env_file_encoding="utf-8",
        extra="ignore",
    )

settings = Settings()