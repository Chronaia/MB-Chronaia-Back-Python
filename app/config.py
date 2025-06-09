from dotenv import load_dotenv
import os

load_dotenv()

DEFAULT_APP_PORT = 8000
DEFAULT_DB_PORT = 5432

def get_env_variable(key, default=None, cast_type=str):
    value = os.getenv(key)
    if value is None:
        return default
    try:
        return cast_type(value)
    except (ValueError, TypeError):
        raise ValueError(f"Environment variable {key} could not be cast to {cast_type}")

class Settings:
    class AppConfig:
        NAME = get_env_variable("APP_NAME", default="App")
        ENV = get_env_variable("APP_ENV", default="development")
        HOST = get_env_variable("APP_HOST", default="127.0.0.1")
        PORT = get_env_variable("APP_PORT", default=DEFAULT_APP_PORT, cast_type=int)

    class DBConfig:
        HOST = get_env_variable("DB_HOST", default="localhost")
        PORT = get_env_variable("DB_PORT", default=DEFAULT_DB_PORT, cast_type=int)
        NAME = get_env_variable("DB_NAME", default="db")
        USER = get_env_variable("DB_USER", default="user")
        PASSWORD = get_env_variable("DB_PASSWORD", default="password")

    SECRET_KEY = get_env_variable("SECRET_KEY", default="changeme")

settings = Settings()