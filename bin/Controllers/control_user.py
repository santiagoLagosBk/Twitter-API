# Data Base
from bin.Config.db_setting import conn
from bin.Models.schema.sche_user import user_query

# Model
from bin.Models.model_user import  UserBase

# FastAPI
from fastapi import HTTPException,status


class Controller_user:


    def create_wrapper(func):

        def wrapper(self,*args):
        
            result = conn.execute(user_query.select().where(user_query.c.email == args[0]["email"])).first()
    
            if result:
                return HTTPException(status.HTTP_400_BAD_REQUEST)
            else:
                func(self,args)

        return wrapper


    @create_wrapper
    def create_user(self,user:UserBase):
        result = conn.execute(user_query.insert().values(user))
        return result

