from fastapi import FastAPI
from app.database import Base, engine
from app.routers import users, items

Base.metadata.create_all(bind=engine)

app = FastAPI()
app.include_router(users.router, prefix="/users", tags=["users"])
app.include_router(items.router, prefix="/items", tags=["items"])
