
from bin.Config.db_setting import conn

from bin.Models.schema.sche_tweets import Tweet
from bin.Models.schema.sche_user import user_query
from sqlalchemy import select
from uuid import uuid4

from fastapi import HTTPException,status


from bin.Models.model_tweet import db_Tweet as Db_tweet

class Controller_tweet:

    def _find_creator(self,nickname):
        
        try:
            user_id = conn.execute(select([user_query.c.id]).where(user_query.c.nickname == nickname)).first()
            if not user_id:
                raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)

            return user_id
        except HTTPException as f:
            return f

        

    def create_tweet(self,content,nickname):

        foreing = self._find_creator(nickname)
        
        dict_tweet = {"id":uuid4(),"create_by":foreing[0],"content":content}
        new_tweet = Db_tweet(**dict_tweet)
    
        result = conn.execute(Tweet.insert().values(new_tweet.dict()))
        return result
    