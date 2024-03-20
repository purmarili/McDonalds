import random
from typing import List

from db.dto.user_order_dto import UserOrderDto
from db.models import UserOrder
from db.repositories.base_repository import BaseRepository


class UserOrderRepository(BaseRepository):

    def get_by_user(self, user_id: int, db) -> List[UserOrderDto]:
        results = db.session.query(UserOrder).filter(UserOrder.user_id == user_id).all()
        return [
            UserOrderDto(
                id=r.id,
                user_id=r.user_id,
                details=r.details,
                date=r.date,
                preparation_time=r.preparation_time
            )
            for r in results
        ]

    def get_all(self, db) -> List[UserOrderDto]:
        results = db.session.query(UserOrder).all()
        return [
            UserOrderDto(
                id=r.id,
                user_id=r.user_id,
                details=r.details,
                date=r.date,
                preparation_time=r.preparation_time
            )
            for r in results
        ]

    def add(self, details: str, user_id: int, db):
        db.session.add(
            UserOrder(
                user_id=user_id,
                details=details,
                preparation_time=random.randint(30, 90)
            )
        )
        db.session.commit()

    def delete(self, order_id: int, db):
        order = db.session.query(UserOrder).filter(
            UserOrder.id == order_id
        ).one_or_none()
        db.session.delete(order)
        db.session.commit()

    def get_by_id(self, id_: int, db):
        order = db.session.query(UserOrder).filter(
            UserOrder.id == id_
        ).one_or_none()
        return UserOrderDto(
            id=order.id,
            user_id=order.user_id,
            details=order.details,
            date=order.date,
            preparation_time=order.preparation_time
        ) if order else None
