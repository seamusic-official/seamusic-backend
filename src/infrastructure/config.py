from pydantic import Field, EmailStr
from pydantic_settings import BaseSettings


class Settings(BaseSettings):

    # model_config = SettingsConfigDict(env_file_encoding='utf-8')

    root_url: str = Field(default='http://localhost:8000', alias='ROOT_URL')

    yandex_cloud_oauth_token: str = Field(default='', alias='YANDEX_CLOUD_OAUTH_TOKEN')
    yandex_cloud_id: str = Field(default='', alias='YANDEX_CLOUD_ID')
    aws_access_key_id: str = Field(default='', alias='AWS_ACCESS_KEY_ID')
    aws_secret_access_key: str = Field(default='', alias='AWS_SECRET_ACCESS_KEY')
    bucket_name: str = Field(default='', alias='BUCKET_NAME')

    spotify_client_id: str = Field(default='', alias='SPOTIFY_CLIENT_ID')
    spotify_client_secret: str = Field(default='', alias='SPOTIFY_CLIENT_SECRET')
    spotify_redirect_uri: str = Field(default='', alias='SPOTIFY_REDIRECT_URI')

    db_host: str = Field(default='localhost', alias='DB_HOST')
    db_port: int = Field(default=5432, alias='DB_PORT')
    db_name: str = Field(default='postgres', alias='DB_NAME')
    db_user: str = Field(default='postgres', alias='DB_USER')
    db_pass: str = Field(default='postgres', alias='DB_PASS')

    redis_host: str = Field(default='localhost', alias='REDIS_HOST')
    redis_port: int = Field(default=6379, alias='REDIS_PORT')
    redis_pass: str = Field(default='qwerty', alias='REDIS_PASS')

    echo: bool = True

    jwt_secret_key: str = Field(default='', alias='JWT_SECRET_KEY')
    jwt_refresh_secret_key: str = Field(default='', alias='JWT_REFRESH_SECRET_KEY')

    email_address: EmailStr = Field(default='seamusimgmt@gmail.com', alias='EMAIL_ADDRESS')
    email_password: str = Field(default='', alias='EMAIL_PASSWORD')
    smtp_host: str = Field(default='', alias='SMTP_HOST')
    smtp_port: int = Field(default=0, alias='SMTP_PORT')

    @property
    def db_url(self) -> str:
        return f"postgresql+asyncpg://{self.db_user}:{self.db_pass}@{self.db_host}:{self.db_port}/{self.db_name}"


settings = Settings()
