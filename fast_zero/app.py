from fastapi import FastAPI

from .routers.auth import auth_router
from .routers.users import user_router

app = FastAPI()
app.include_router(user_router)
app.include_router(auth_router)
