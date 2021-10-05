from faker import Faker
import pytest

from app.users import users_api

fake = Faker()

@pytest.fixture
def create_a_user():
    user = users_api.post(fake.first_name(), fake.last_name()).json()
    yield user
    users_api.delete('api/users/'+user['id']) 