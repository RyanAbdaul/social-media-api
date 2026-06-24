from fastapi.testclient import TestClient
from app.main import app
import pytest
from app import schemas, models
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from app.database import get_db, Base
from app.oauth2 import create_access_token
SQLALCHEMY_DATABASE_URL = 'postgresql+psycopg://ryanabdaulaziz@localhost:5433/fastapi_test'

engine = create_engine(SQLALCHEMY_DATABASE_URL)

TestSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# -------- Main Fixtures Start ------------------------------------------------------------------------------------------------------
@pytest.fixture()
def session():
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)
    db = TestSessionLocal()
    try:
        yield db
    finally:
        db.close()

@pytest.fixture()
def client(session):
    def override_get_db():
        try:
            yield session
        finally:
            session.close()
    app.dependency_overrides[get_db] = override_get_db
    yield TestClient(app)

# -------- Main Fixtures End ------------------------------------------------------------------------------------------------------



# -------- Users Fixtures Start ------------------------------------------------------------------------------------------------------

@pytest.fixture
def _test_user(client):
    test_user = {
        'email': 'hello123@gmail.com',
        'password': '123'
    }
    res = client.post('/users/', json=test_user)

    assert res.status_code == 201
    new_user = res.json()
    new_user['password'] = test_user['password']
    return new_user

@pytest.fixture
def _token(_test_user):
    return create_access_token({'user_id': _test_user['id']})

@pytest.fixture
def authorized_client(client, _token):
    client.headers = {
        **client.headers,
        "Authorization": f"Bearer {_token}"
    }
    return client
# -------- Users Fixtures End ------------------------------------------------------------------------------------------------------


# -------- Posts Fixtures Start ------------------------------------------------------------------------------------------------------

@pytest.fixture
def _test_posts(_test_user, session):
    posts_data = [
        {
            'title': 'Test1',
            'content': 'Blablablablablablabla',
            'user_id': _test_user['id']
        },
        {
            'title': 'Test2',
            'content': 'Blablablablablablabla',
            'user_id': _test_user['id']
        },
        {
            'title': 'Test3',
            'content': 'Blablablablablablabla',
            'user_id': _test_user['id']
        },
        {
            'title': 'Test4',
            'content': 'Blablablablablablabla',
            'user_id': _test_user['id']
        },
        {
            'title': 'Test5',
            'content': 'Blablablablablablabla',
            'user_id': _test_user['id']
        }
    ]
    
    def create_posts_models(posts):
        return models.Post(**posts)
    
    posts = map(create_posts_models, posts_data)
    session.add_all(posts)
    session.commit()
    
    posts = session.query(models.Post).all()
    return posts

# -------- Posts  Fixtures End ------------------------------------------------------------------------------------------------------