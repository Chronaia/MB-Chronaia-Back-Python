from fastapi import FastAPI
from app.config import settings
from app.api.routes import router as api_router

app = FastAPI(title=settings.AppConfig.NAME)

app.include_router(api_router)