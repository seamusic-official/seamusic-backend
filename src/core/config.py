from pydantic import Field, EmailStr
from pydantic_settings import BaseSettings, SettingsConfigDict

from src.core.loggers import core as logger


class Settings(BaseSettings):

    model_config = SettingsConfigDict(env_file='.env', env_file_encoding='utf-8')

    root_url: str = Field(default='http://localhost:8000', alias='ROOT_URL')

    yandex_cloud_oauth_token: str = Field(default='', alias='YANDEX_CLOUD_OAUTH_TOKEN')
    yandex_cloud_id: str = Field(default='', alias='YANDEX_CLOUD_ID')
    aws_access_key_id: str = Field(default='', alias='AWS_ACCESS_KEY_ID')
    aws_secret_access_key: str = Field(default='', alias='AWS_SECRET_ACCESS_KEY')

    spotify_client_id: str = Field(default='', alias='SPOTIFY_CLIENT_ID')
    spotify_client_secret: str = Field(default='', alias='SPOTIFY_CLIENT_SECRET')
    spotify_redirect_uri: str = Field(default='', alias='SPOTIFY_REDIRECT_URI')

    db_host: str = Field(default='localhost', alias='DB_HOST')
    db_port: int = Field(default=5432, alias='DB_PORT')
    db_name: str = Field(default='postgres', alias='DB_NAME')
    db_user: str = Field(default='postgres', alias='DB_USER')
    db_pass: str = Field(default='postgres', alias='DB_PASS')

    db_host_test: str = Field(default='localhost', alias='DB_HOST_TEST')
    db_port_test: int = Field(default=6000, alias='DB_PORT_TEST')
    db_name_test: str = Field(default='postgres', alias='DB_NAME_TEST')
    db_user_test: str = Field(default='postgres', alias='DB_USER_TEST')
    db_pass_test: str = Field(default='postgres', alias='DB_PASS_TEST')

    redis_host: str = Field(default='localhost', alias='REDIS_HOST')
    redis_port: int = Field(default=6379, alias='REDIS_PORT')
    redis_pass: str = Field(default='qwerty', alias='REDIS_PASS')

    redis_host_test: str = Field(default='localhost', alias='REDIS_HOST_TEST')
    redis_port_test: int = Field(default=6379, alias='REDIS_PORT_TEST')
    redis_pass_test: str = Field(default='qwerty', alias='REDIS_PASS_TEST')

    echo: bool = True

    jwt_secret_key: str = Field(default='', alias='JWT_SECRET_KEY')
    jwt_refresh_secret_key: str = Field(default='', alias='JWT_REFRESH_SECRET_KEY')

    bucket_name: str = Field(default='', alias='BUCKET_NAME')

    email_address: EmailStr = Field(default='seamusimgmt@gmail.com', alias='EMAIL_ADDRESS')
    email_password: str = Field(default='', alias='EMAIL_PASSWORD')
    smtp_host: str = Field(default='', alias='SMTP_HOST')
    smtp_port: int = Field(default=0, alias='SMTP_PORT')

    @property
    def db_url(self) -> str:
        return f"postgresql+asyncpg://{self.db_user}:{self.db_pass}@{self.db_host}:{self.db_port}/{self.db_name}"

    @property
    def db_url_test(self) -> str:
        return f'postgresql+asyncpg://{self.db_user_test}:{self.db_pass_test}@{self.db_host_test}:{self.db_port_test}/{self.db_name_test}'


settings = Settings()

logger.debug(f'''Database settings:
host={settings.db_host}
port={settings.db_port}
name={settings.db_name}
username={settings.db_user}
password={settings.db_pass}
url={settings.db_url}''')
