from typing import Optional
from fastapi import APIRouter
from fastapi import status
from fastapi import Form
from fastapi.param_functions import Query



from bin.Controllers.control_tweet import Controller_tweet
from bin.Models.model_tweet import Show_Tweet
twitter_rout = APIRouter()


@twitter_rout.post(path="/twitter/post",tags=["twitter"],status_code=status.HTTP_201_CREATED,summary="Create tweet")
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



@twitter_rout.get(path="/Twitter/Home",tags=["twitter"],status_code=status.HTTP_200_OK,summary="get an expecific tweet or all of them")
def get_tweet(tweet_id:Optional[str] = Query(default= None,min_length=8,max_length=60)):
    controller = Controller_tweet()
    result = controller.show_tweet(tweet_id)
    return result

    

    