import pytest


def test_home_page(client):
    response = client.get('/')
    assert response.status_code == 302


def test_all_orders(client):
    response = client.get('/all_orders')
    assert response.status_code == 200


@pytest.mark.order(1)
def test_registration(client, db_test, user_repository):
    form_data = {'username': 'jemali', 'password': 'password123', 'email': 'jemali@gmail.com'}
    response = client.post('/register', data=form_data)
    res = user_repository.get_all(db_test)
    assert len(res) == 1
    assert res[0].username == 'jemali'
    assert response.status_code == 302


@pytest.mark.order(2)
def test_login(client, db_test, user_repository):
    form_data = {'username': 'jemali', 'password': 'password123'}
    response = client.post('/login', data=form_data)
    assert response.status_code == 302


@pytest.mark.order(3)
def test_order(client, db_test, user_order_repository):
    response = client.post('/order', data={'details': 'burger'})
    assert response.status_code == 302
    result = user_order_repository.get_all(db_test)
    assert len(result) == 1
    assert result[0].details == 'burger'


@pytest.mark.order(4)
def test_all_orders_post(client, db_test, user_order_repository):
    response = client.get('/all_orders')
    assert response.status_code == 200
    result = user_order_repository.get_all(db_test)
    assert len(result) == 1
    assert result[0].details == 'burger'


@pytest.mark.order(5)
def test_orders(client, db_test, user_order_repository):
    response = client.get('/orders')
    assert response.status_code == 200
    result = user_order_repository.get_all(db_test)
    assert len(result) == 1
    assert result[0].details == 'burger'


@pytest.mark.order(6)
def test_orders(client, db_test, user_order_repository):
    response = client.post('/delete/1')
    assert response.status_code == 302
    result = user_order_repository.get_all(db_test)
    assert len(result) == 0
