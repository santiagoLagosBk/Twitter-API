# FastAPI
from fastapi import FastAPI

# Routes
from bin.Routers.rout_user import user_route

app = FastAPI()

app.include_router(user_route)
