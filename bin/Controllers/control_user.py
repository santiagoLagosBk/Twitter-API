# Data Base

from sqlalchemy.sql.expression import delete
from bin.Config.db_setting import conn
from bin.Models.schema.sche_user import user_query
from sqlalchemy import select

# Model
from bin.Models.model_user import  User, UserBase

# FastAPI
from fastapi import HTTPException,status


class Controller_user:

    COlUMNS = [user_query.c.fist_name,user_query.c.last_name,user_query.c.nickname,user_query.c.birth_date]

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


    def get_user(self,nick_name:str):
        
        try:
            result = conn.execute(select(self.COlUMNS).where(user_query.c.nickname == nick_name)).first()
            if result:
                user = User(**result)
                return user
            else:
                raise HTTPException(status_code= status.HTTP_404_NOT_FOUND)
                
        except ValueError as f:
            print(f)

    

    def get_all_users(self):
        
        all_users = []
        result = conn.execute(select(self.COlUMNS))
        for i in result:
            new_user = User(**i)
            all_users.append(new_user.dict())
        return all_users


    def delete(self,id:str):
        result = conn.execute(user_query.delete().where(user_query.c.id == id))
        return result