from typing import Optional, List

from sqlalchemy import or_

from db.dto.user_dto import UserDto
from db.models import User
from db.repositories.base_repository import BaseRepository


class UserRepository(BaseRepository):

    def get(self, id_: Optional[int] = None, username: Optional[str] = None, email: Optional[str] = None, db=None) \
            -> Optional[UserDto]:
        conditions = []
        if id_:
            conditions.append(User.id == id_)
        if username:
            conditions.append(User.username == username)
        if email:
            conditions.append(User.email == email)

        if not conditions:
            return None

        result = db.session.query(User).filter(or_(*conditions)).first()
        if result:
            return UserDto.model_validate(result)
        return None

    def get_all(self, db) -> List[UserDto]:
        results = db.session.query(User).all()
        return [
            UserDto.model_validate(r)
            for r in results
        ]

    def add(self, user_name: str, email: str, password: str, db):
        result = db.session.query(User).filter(
            User.username == user_name, User.email == email
        ).first()
        if result:
            raise Exception('User Already Exists!')
        db.session.add(User(
            username=user_name,
            email=email,
            hashed_password=password
        ))
        db.session.commit()
