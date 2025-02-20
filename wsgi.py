import uvicorn

import config
import application

app = application.create_app()

if __name__ == "__main__":
    conf = config.get_config()
    uvicorn.run(app, host=conf.host, port=conf.port, reload = True)