from fastapi import APIRouter
from app.core.status import get_status_message

router = APIRouter()

@router.get("/", tags=["System"])
def get_app_status():
    return get_status_message()