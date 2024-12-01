from fastapi import FastAPI

from src.api import utils, contacts

app = FastAPI()

API_PREFIX = "/api"
app.include_router(utils.router, prefix=API_PREFIX)
app.include_router(contacts.router, prefix=API_PREFIX)

if __name__ == "__main__":
    import uvicorn

    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
