import pytest

from app import create_app
from db.database import db
from db.repositories.cast_repository import CastRepository
from db.repositories.movie_cast_repository import MovieCastRepository
from db.repositories.movie_repository import MovieRepository
from db.repositories.user_orders_repository import UserOrderRepository
from db.repositories.user_repository import UserRepository


@pytest.fixture(scope='module')
def numbers():
    return [i for i in range(10)]


@pytest.fixture(scope='module')
def client():
    app = create_app()
    app.config.update({
        'SQLALCHEMY_DATABASE_URI': 'sqlite:///:memory:',
        'SECRET_KEY': 'paroli'
    })

    with app.app_context():
        db.create_all()

    with app.test_client() as testing_client:
        with app.app_context():
            yield testing_client

    with app.app_context():
        db.drop_all()


@pytest.fixture(scope='module')
def db_test():
    return db


@pytest.fixture(scope='module')
def user_repository():
    return UserRepository()


@pytest.fixture(scope='module')
def movie_repository():
    return MovieRepository()


@pytest.fixture(scope='module')
def user_order_repository():
    return UserOrderRepository()


@pytest.fixture(scope='module')
def cast_repository():
    return CastRepository()


@pytest.fixture(scope='module')
def movie_cast_repository():
    return MovieCastRepository()
