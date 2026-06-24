from app import schemas
import pytest
import jwt
from app.config import settings
'''
    To run the tests run "test_program"
'''




def test_user_creation(client):
    res = client.post('/users/', json={
        'email': 'hello123@gmail.com',
        'password': '123'
    })
    new_user = schemas.UserOut(**res.json())
    assert new_user.email == 'hello123@gmail.com'
    assert res.status_code == 201

def test_login_user(client, _test_user):
    res = client.post('/login', data={
        'username': _test_user['email'],
        'password': _test_user['password']
    })
    
    login_res = schemas.Token(**res.json())
    payload = jwt.decode(login_res.access_token, settings.secret_key, settings.algorithm)
    
    id = payload.get('user_id')
    assert id == _test_user['id']
    assert login_res.token_type == 'bearer'
    assert res.status_code == 200

@pytest.mark.parametrize("email, password, status_code", [
    ('hello123@gmail.com', '123456', 403),
    ('helloworld@gmail.com', '123', 403),
    ('helloworld@gmail.com', '1234444', 403),
    ('helloworld@gmail.com', None, 422),
    (None, '123', 422),
    
])
def test_incorrect_login(client, _test_user, email, password, status_code):
    res = client.post('/login', data={
        'username': email,
        'password': password,
    })
    assert res.status_code == status_code