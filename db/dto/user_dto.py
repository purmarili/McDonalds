import datetime
from typing import Optional

from pydantic import BaseModel


class UserDto(BaseModel):
    id: int
    username: Optional[str] = None
    email: Optional[str] = None
    hashed_password: Optional[str] = None
    create_date: Optional[datetime.datetime] = None
