from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from segunda_questao.src.controllers import users_controllers
from segunda_questao.src.utils.logger import logger
from contextlib import asynccontextmanager

APP_NAME = "Valcann Users API"


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup
    logger.info(f"Starting {APP_NAME}")
    yield
    # Shutdown
    logger.info(f"Shutting down {APP_NAME}")


app = FastAPI(title=APP_NAME, lifespan=lifespan)

# Configurar CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # em produção, restrinja!
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Rotas
app.include_router(users_controllers.router)
