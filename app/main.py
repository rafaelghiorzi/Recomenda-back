".venv/Scripts/activate"
"fastapi dev main.py"

from contextlib import asynccontextmanager
from fastapi import FastAPI
from .utils.prisma import connect, disconnect
from .routers.user import user_router

@asynccontextmanager
async def lifespan(app: FastAPI):
    print("Startup")
    await connect()
    yield
    print("Shutdown")
    await disconnect()

app = FastAPI(lifespan=lifespan)
app.include_router(user_router)

@app.get("/")
async def root():
    return {"message": "Hello World"}
