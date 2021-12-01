from fastapi import APIRouter
from fastapi import status
from fastapi import Form

from bin.Models.model_tweet import ShowTweet

from bin.Controllers.control_tweet import Controller_tweet
twitter_rout = APIRouter()


@twitter_rout.post(path="/twitter/create",tags=["twitter"],status_code=status.HTTP_201_CREATED,summary="Create tweet")
def create_tweet(content: str = Form(
    ...,
    max_length=256
    ),
    nickname:str = Form(
    ...,
    min_length=2,
    max_length=20)):

    controller = Controller_tweet()
    result = controller.create_tweet(content,nickname)
    return result
    

    