import datetime
from typing import Optional

from pydantic import BaseModel, ConfigDict


class UserDto(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    username: Optional[str] = None
    email: Optional[str] = None
    hashed_password: Optional[str] = None
    create_date: Optional[datetime.datetime] = None
