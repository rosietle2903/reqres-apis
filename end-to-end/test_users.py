import pytest

from faker import Faker

from app.users import users_api
from fixtures.users_fixtures import create_a_user

fake = Faker()

def test_creating_users_with_valid_login():
    payload = users_api.create_a_user_payload(fake.first_name(), fake.last_name())
    resp = users_api.post('/api/users.json', payload)
    assert resp.status_code == 201
    

