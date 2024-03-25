import datetime
import json

from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Float

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
    create_date = Column(DateTime, nullable=False, default=datetime.datetime.now)


class Movie(db.Model):
    __tablename__ = 'movies'
    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    year = Column(Integer, nullable=False)
    time = Column(String, nullable=False)
    rating = Column(Float, nullable=False)
    rating_count = Column(String, nullable=False)
    top_250_rating = Column(Integer, nullable=False)
    image_url = Column(String, nullable=True)
    create_date = Column(DateTime, nullable=False, default=datetime.datetime.now)


class Cast(db.Model):
    __tablename__ = 'cast'
    id = Column(Integer, primary_key=True)
    full_name = Column(String, nullable=False)
    movie_names = Column(String)
    image_url = Column(String, nullable=True)
    create_date = Column(DateTime, nullable=False, default=datetime.datetime.now)

    @property
    def movie_names_list(self):
        return json.loads(self.movie_names)

    @movie_names_list.setter
    def movie_names_list(self, value):
        self.movie_names = json.dumps(value)


class MovieCast(db.Model):
    __tablename__ = 'movie_cast'
    id = Column(Integer, primary_key=True)
    movie_id = Column(Integer, ForeignKey('movies.id'))
    cast_id = Column(Integer, ForeignKey('cast.id'))
    create_date = Column(DateTime, nullable=False, default=datetime.datetime.now)
