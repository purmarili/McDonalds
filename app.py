from datetime import timedelta, datetime

from flask import Flask, session, redirect, url_for, render_template, request

from db.dto.user_dto import UserDto
from db.models import *
from db.repositories.user_orders_repository import UserOrderRepository
from db.repositories.user_repository import UserRepository
from models.enums import SessionKeyEnum
from utils import check_password, get_hashed_password


def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///instance/mcdonalds.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SECRET_KEY'] = 'password'
    app.permanent_session_lifetime = timedelta(hours=2)

    db.init_app(app)

    with app.app_context():
        db.create_all()

    user_repository = UserRepository()
    user_order_repository = UserOrderRepository()

    @app.route('/')
    def home():
        if SessionKeyEnum.AUTHORIZED.value in session:
            return redirect(url_for('orders'))
        return redirect(url_for('all_orders'))

    @app.route('/order', methods=['GET', 'POST'])
    def order():
        if SessionKeyEnum.AUTHORIZED.value not in session:
            return redirect(url_for('home'))
        if request.method == 'GET':
            return render_template('order.html', session=session)
        details = request.form.get('details')
        if details == '' or details is None:
            return redirect(url_for('order'))

        user_order_repository.add(details=details, user_id=session.get(SessionKeyEnum.ID.value), db=db)
        return redirect(url_for('orders'))

    @app.route('/all_orders')
    def all_orders():
        results = user_order_repository.get_all(db=db)
        ready = list(
            filter(lambda x: x.date + timedelta(seconds=x.preparation_time) < datetime.datetime.now(), results))
        preparing = list(filter(lambda x: x.id not in [r.id for r in ready], results))
        return render_template('all_orders.html', preparing=preparing, ready=ready, session=session)

    @app.route('/orders')
    def orders():
        if SessionKeyEnum.AUTHORIZED.value not in session:
            return redirect(url_for('home'))
        user_id = session.get(SessionKeyEnum.ID.value)
        results = user_order_repository.get_by_user(user_id=user_id, db=db)
        return render_template('orders.html', orders=results, session=session)

    @app.route('/login', methods=['GET', 'POST'])
    def login():
        if request.method == 'GET':
            if SessionKeyEnum.AUTHORIZED.value in session:
                return redirect(url_for('home'))
            return render_template('login.html', session=session)

        username = request.form.get('username', None)
        password = request.form.get('password', None)
        user = user_repository.get(username=username, db=db)
        if user:
            if check_password(password=password, hashed_password=user.hashed_password):
                assign_session_keys(user=user)
                return redirect(url_for('home'))

        return redirect(url_for('login'))

    @app.route('/register', methods=['GET', 'POST'])
    def register():
        if request.method == 'GET':
            if SessionKeyEnum.AUTHORIZED.value in session:
                return redirect(url_for('home'))
            return render_template('register.html', session=session)

        username = request.form.get('username', None)
        email = request.form.get('email', None)
        password = request.form.get('password', None)
        user = user_repository.get(username=username, email=email, db=db)
        if user:
            return redirect(url_for('register'))
        else:
            user_repository.add(
                user_name=username, email=email, password=get_hashed_password(password=password), db=db
            )

        return redirect(url_for('login'))

    @app.route('/delete/<int:order_id>', methods=['POST'])
    def delete(order_id: int):
        if SessionKeyEnum.AUTHORIZED.value not in session:
            return redirect(url_for('home'))

        user_order = user_order_repository.get_by_id(id_=order_id, db=db)
        if user_order and user_order.user_id == session[SessionKeyEnum.ID.value]:
            user_order_repository.delete(order_id, db=db)

        return redirect(url_for('orders'))

    @app.route('/logout')
    def logout():
        clear_session_keys()
        return redirect(url_for('home'))

    def assign_session_keys(user: UserDto):
        session[SessionKeyEnum.ID.value] = user.id
        session[SessionKeyEnum.USERNAME.value] = user.username
        session[SessionKeyEnum.AUTHORIZED.value] = True

    def clear_session_keys():
        session.pop(SessionKeyEnum.ID.value, None)
        session.pop(SessionKeyEnum.USERNAME.value, None)
        session.pop(SessionKeyEnum.AUTHORIZED.value, None)

    return app


if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
