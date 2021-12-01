# FastAPI
from fastapi import FastAPI

# Routes
from bin.Routers.rout_user import user_route
from bin.Routers.router_twitter import twitter_rout

app = FastAPI()

app.include_router(user_route)
app.include_router(twitter_rout)

