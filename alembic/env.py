import os
import sys
from logging.config import fileConfig
from urllib.parse import quote_plus
from sqlalchemy import engine_from_config, pool, QueuePool
from alembic import context

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from dotenv import load_dotenv
load_dotenv()

from app.config import settings
from app.models import Base
from app import models

# Configuration de la metadata pour les migrations
target_metadata = Base.metadata

def get_url():
    user = quote_plus(settings.DBConfig.USER)
    pwd = quote_plus(settings.DBConfig.PASSWORD)
    host = settings.DBConfig.HOST
    port = settings.DBConfig.PORT
    db   = settings.DBConfig.NAME

    return f"postgresql+psycopg://{user}:{pwd}@{host}:{port}/{db}"

# Configuration dynamique de l'URL de BDD
config = context.config
config.set_main_option("sqlalchemy.url", get_url())

# Logging config
if config.config_file_name is not None:
    fileConfig(config.config_file_name)


# other values from the config, defined by the needs of env.py,
# can be acquired:
# my_important_option = config.get_main_option("my_important_option")
# ... etc.


def run_migrations_offline() -> None:
    """Run migrations in 'offline' mode.

    This configures the context with just a URL
    and not an Engine, though an Engine is acceptable
    here as well.  By skipping the Engine creation
    we don't even need a DBAPI to be available.

    Calls to context.execute() here emit the given string to the
    script output.

    """
    url = config.get_main_option("sqlalchemy.url")
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()

def run_migrations_online() -> None:
    connectable = engine_from_config(
        config.get_section(config.config_ini_section),
        prefix="sqlalchemy.",
        poolclass=QueuePool,
        url=get_url()
    )

    with connectable.connect() as connection:
        context.configure(
            connection=connection, target_metadata=target_metadata
        )

        with context.begin_transaction():
            context.run_migrations()


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
