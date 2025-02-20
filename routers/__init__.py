from fastapi import APIRouter
from fastapi.staticfiles import StaticFiles

from .clients import clients_router

main_router = APIRouter()
main_router.mount('/static', StaticFiles(directory='static'), name='static')
main_router.include_router(clients_router, prefix='/clients')