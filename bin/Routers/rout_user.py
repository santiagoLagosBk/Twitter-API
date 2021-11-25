# FastApi
from fastapi import APIRouter
from fastapi import status
from fastapi import Form,Body


# Python
from typing import Optional



user_route = APIRouter()

@user_route.get(path="/",tags=["User"],status_code=status.HTTP_200_OK)
def home():
    return {"TwitterApp":"Working"}


@user_route.post(path="/Signup",tags=["User"],status_code=status.HTTP_201_CREATED)
def create_user():
    pass


@user_route.get(path="/users/",status_code=status.HTTP_200_OK)
def get_user(user:Optional[str] = None):
    if not user:
        pass
    

