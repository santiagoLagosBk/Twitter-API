# ORM
from pydantic import BaseModel,Field
from pydantic import EmailStr

# PYTHON
from uuid import UUID,uuid4
from datetime import date

from pydantic.types import UUID


    
class User(BaseModel):

    fist_name: str = Field(...,
        min_length=1,
        max_length=50,
    )
    last_name:str = Field(...,
        min_length=1,
        max_length=45
    )
    nickname:str = Field(...,
        min_length=1,
        max_length=20
    )
    birth_date: date = Field(...)

class UserLogin(User):
    email: EmailStr = Field(...)
    password: str = Field(...,
    min_length=8
    )

class  UserBase(UserLogin):
    id: UUID = Field(uuid4())    



