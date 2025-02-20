
import routers
from fastapi import FastAPI


def create_app() -> FastAPI:
    async def lifespan(app: FastAPI):
        # do something before start
        yield
        # do something after stop

    app = FastAPI(title='RL monitoring', lifespan=lifespan)
    app.include_router(routers.main_router)
    return app