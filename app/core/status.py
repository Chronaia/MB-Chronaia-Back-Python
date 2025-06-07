from app.config import settings

APP_STATUS_MESSAGE_TEMPLATE = "{} is running in {} mode."

def get_status_message():
    return {
        "message": APP_STATUS_MESSAGE_TEMPLATE.format(
            settings.AppConfig.NAME,
            settings.AppConfig.ENV
        )
    }