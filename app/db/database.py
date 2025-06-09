from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.config import settings

DB_URL = (
    f"postgresql+psycopg://{settings.DBConfig.USER}:{settings.DBConfig.PASSWORD}"
    f"@{settings.DBConfig.HOST}:{settings.DBConfig.PORT}/{settings.DBConfig.NAME}"
)

engine = create_engine(DB_URL, echo=False, future=True, pool_pre_ping=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)