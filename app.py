import logging
from fastapi import FastAPI
from prometheus_fastapi_instrumentator import Instrumentator

app = FastAPI()
logging.basicConfig(
    handlers=[
        logging.FileHandler("/var/log/app.log"),
        logging.StreamHandler()
    ]
)


@app.on_event("startup")
def startup():
    Instrumentator().instrument(app).expose(app)


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/ouch")
def read_ouch():
    logging.error("ouch")
    return {"Ouch": "Something went wrong"}
