
from os import stat
from typing import Optional
from bin.Config.db_setting import conn
from bin.Models.model_user import User

from bin.Models.schema.sche_tweets import Tweet
from bin.Models.schema.sche_user import user_query
from sqlalchemy import select
from sqlalchemy.orm.exc import NoResultFound
from uuid import uuid4

from fastapi import HTTPException,status


from bin.Models.model_tweet import Db_Tweet
from bin.Models.model_tweet import Show_Tweet

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
        new_tweet = Db_Tweet(**dict_tweet)
    
        result = conn.execute(Tweet.insert().values(new_tweet.dict()))
        return result
    

    def show_tweet(self,tweet_id:Optional[str]):
        
        user_fields = [user_query.c.nickname,user_query.c.fist_name,user_query.c.last_name,user_query.c.birth_date]
        if tweet_id:
            try:
                tweet_db = conn.execute(Tweet.select().where(Tweet.c.id == tweet_id)).first()
                if not tweet_db:
                    raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                    detail="The tweet element was not found by that ID try with another")

            except HTTPException as f:
                return f
            
            
            new_tweet = Db_Tweet(**tweet_db)
            user_id = new_tweet.dict()["create_by"]
            tweet_user = conn.execute(select(user_fields).where(user_query.c.id == user_id)).first()
            create_by = User(**tweet_user)

            twitter_dict = new_tweet.dict()
            twitter_dict.update({"create_by":create_by.dict()})
            
            result = Show_Tweet(**twitter_dict)
            return result
        else:

            tweets = conn.execute(Tweet.select())
            all_tweets = []
            for tweet in tweets:
                tweetdb = Db_Tweet(**tweet)
                user_id = tweetdb.dict()["create_by"]
                tweet_user = conn.execute(select(user_fields).where(user_query.c.id == user_id)).first()
                create_by = User(**tweet_user)
                tweet_dict = tweetdb.dict()
                tweet_dict.update({"create_by":create_by.dict()})

                result = Show_Tweet(**tweet_dict)
                all_tweets.append(result)
            return all_tweets