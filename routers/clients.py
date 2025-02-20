from fastapi import APIRouter
import config

clients_router = APIRouter()


@clients_router.get("")
async def get_clients():
    # conf = config.get_config()
    return {"clients": [{"id": 1, "name": "Alice"}, {"id": 2, "name": "Bob"}]}
