import datetime
from typing import Optional

from pydantic import BaseModel


class UserOrderDto(BaseModel):
    id: int
    user_id: Optional[int] = None
    details: Optional[str] = None
    date: Optional[datetime.datetime] = None
    preparation_time: Optional[int] = None
