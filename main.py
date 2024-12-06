".venv/Scripts/activate"
"fastapi dev main.py"

from contextlib import asynccontextmanager
from fastapi import FastAPI
from app.core.prisma import connect, disconnect
from app.api.routes import user_routes, movie_routes, rating_routes, tag_routes

@asynccontextmanager
async def lifespan(app: FastAPI):
    print("Startup")
    await connect()
    yield
    print("Shutdown")
    await disconnect()

app = FastAPI(lifespan=lifespan)
app.include_router(user_routes.router, prefix="/users", tags=["users"])
app.include_router(movie_routes.router, prefix="/movies", tags=["movies"])
app.include_router(rating_routes.router, prefix="/ratings", tags=["ratings"])
app.include_router(tag_routes.router, prefix="/tags", tags=["tags"])

@app.get("/")
async def root():
    return {"message": "Hello World"}
