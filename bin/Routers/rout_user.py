# FastApi
from fastapi import APIRouter
from fastapi import status
from fastapi import Form,Body


# Python
from typing import Optional
from uuid import uuid4


# Controller
from bin.Controllers.control_user import Controller_user

# Model
from bin.Models.model_user import UserLogin,UserBase


user_route = APIRouter()

@user_route.get(path="/",tags=["User"],status_code=status.HTTP_200_OK)
def home():
    return {"TwitterApp":"Working"}


@user_route.post(path="/Signup",tags=["User"],status_code=status.HTTP_201_CREATED)

def create_user(user: UserLogin = Body(...)):
    controller = Controller_user()

    user_in_db = UserBase(**user.dict())
    result = controller.create_user(user_in_db.dict())
    
    return result


@user_route.get(path="/users/",status_code=status.HTTP_200_OK)
def get_user(user:Optional[str] = None):
    if not user:
        pass
    

