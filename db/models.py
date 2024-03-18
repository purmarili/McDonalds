import datetime
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey

from .database import db


class User(db.Model):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    username = Column(String, nullable=False, unique=True)
    email = Column(String, nullable=False, unique=True)
    hashed_password = Column(String, nullable=False)
    create_date = Column(DateTime, nullable=False, default=datetime.datetime.now)


class UserOrder(db.Model):
    __tablename__ = 'user_orders'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    details = Column(String, nullable=False)
    date = Column(DateTime, nullable=False, default=datetime.datetime.now)
    preparation_time = Column(Integer, nullable=False)
