from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from segunda_questao.src.controllers import users_controllers
from segunda_questao.src.utils.logger import logger
from contextlib import asynccontextmanager

APP_NAME = "Valcann Users API"


@asynccontextmanager
async def lifespan(app: FastAPI):
    logger.info(f"Starting {APP_NAME}")
    yield
    logger.info(f"Shutting down {APP_NAME}")


app = FastAPI(title=APP_NAME, lifespan=lifespan)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(users_controllers.router)
