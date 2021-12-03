from pydantic import BaseModel
from pydantic import Field

# PYTHON
from uuid import UUID
from datetime import datetime
from typing import Optional

# Format datetime
DATETIME_FORMAT = "%Y-%m-%d %H:%M:%S"

# Models
from bin.Models.model_user import User


class Basic_Tweet(BaseModel):

    content: str = Field(
        ...,
        min_length=1,
        max_length=256)

    create_at: datetime = Field(default=datetime.now().strftime(DATETIME_FORMAT))
    update_at: Optional[datetime] = Field(default=datetime.now().strftime(DATETIME_FORMAT))

class Db_Tweet(Basic_Tweet):
    id: UUID = Field(...)
    create_by: str = Field(...)


class Show_Tweet(Basic_Tweet):
    create_by: User = Field(...)






