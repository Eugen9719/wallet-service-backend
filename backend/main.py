import logging

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from starlette.middleware.cors import CORSMiddleware
from backend.app import routers
from backend.core.config import settings


# Настройка логирования
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Инициализация FastAPI
app = FastAPI(
    title=settings.PROJECT_NAME,
    openapi_url=f"{settings.API_V1_STR}/openapi.json",
    DEBUG=True
)




# Настройки CORS
origins = [
    "http://localhost",
    "http://localhost:4200",
    "http://localhost:3000",
    "http://127.0.0.1:8000",
    "http://127.0.0.1:8080",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Можно ограничить доступ только к определенным доменам
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)




# Подключение маршрутов
app.include_router(routers.api_router, prefix=settings.API_V1_STR)












######################################## Admin #########################################################################

# admin = Admin(app, engine, authentication_backend=authentication_backend)
#
# admin.add_view(UserAdmin)
