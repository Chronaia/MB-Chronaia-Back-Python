from dotenv import load_dotenv
import os

load_dotenv()

DEFAULT_APP_PORT = 8000
DEFAULT_DB_PORT = 5432

def get_env_variable(key, default=None, cast_type=str):
    value = os.getenv(key, default)
    return cast_type(value) if value is not None else None

class Settings:
    class AppConfig:
        NAME = get_env_variable("APP_NAME")
        ENV = get_env_variable("APP_ENV")
        HOST = get_env_variable("APP_HOST")
        PORT = get_env_variable("APP_PORT", default=DEFAULT_APP_PORT, cast_type=int)

    class DBConfig:
        HOST = get_env_variable("DB_HOST")
        PORT = get_env_variable("DB_PORT", default=DEFAULT_DB_PORT, cast_type=int)
        NAME = get_env_variable("DB_NAME")
        USER = get_env_variable("DB_USER")
        PASSWORD = get_env_variable("DB_PASSWORD")

    SECRET_KEY = get_env_variable("SECRET_KEY")

settings = Settings()