from faker import Faker

from app.users import users_api
from fixtures.users_fixtures import create_a_user


fake = Faker()

def test_get_users():
    resp = users_api.get('/api/users.json')
    assert resp.status_code == 200

def test_post_user():
    payload = users_api.create_a_user_payload(fake.first_name(), fake.last_name())
    resp = users_api.post('/api/users.json', payload)
    assert resp.status_code == 201

def test_invalid_register_no_password():
    payload = {
        "email": "sydney@fife"
    }   
    resp = users_api.post('/api/register', payload)
    error = resp.json()["error"]
    assert error == "Missing password"
    assert resp.status_code == 400

def test_invalid_register_wrong_email_format():
    payload = users_api.register_a_user_payload("notAnEmail", "pistol")
    resp = users_api.post('/api/register', payload)
    error = resp.json()["error"]
    assert error == "Note: Only defined users succeed registration"
    assert resp.status_code == 400

def test_valid_register(): 
    payload = users_api.register_a_user_payload("eve.holt@reqres.in", "pistol")
    resp = users_api.post('/api/register', payload)
    token = resp.json()["token"]
    assert token == "QpwL5tke4Pnpja7X4"
    assert resp.status_code == 200

def test_email_password_returns_in_response():
    usr_email = "testing@gmail.com"
    usr_pwd = "testing123"
    payload = users_api.register_a_user_payload(usr_email, usr_pwd)
    resp = users_api.post('/api/register.json', payload)
    email = resp.json()["email"]
    password = resp.json()["password"]
    assert email == usr_email
    assert password == usr_pwd
    assert resp.status_code == 201
    
#This API doesn't return an actual valid ID to retrieve a user. However, for the purpose of demostrating what tests would look like if it does return an ID, I have included them but commented them out. 

# def test_get_user_by_id(create_a_user):
#     resp = users_api.get(f'/api/users/{create_a_user["id"]}.json')
#     assert resp.status_code == 200

# def test_put_user_by_id():
#     payload = users_api.create_a_user_payload(fake.first_name(), fake.last_name())
#     user = users_api.post('/api/users.json', payload)
#     id = user['id']
#     resp = users_api.put('/api/users/{id}', first_name=fake.first_name())
#     assert resp.status_code == 204

# def test_delete_user_by_id(create_a_user):
#     resp = users_api.delete(f'/api/users/{create_a_user["id"]}.json')
#     assert resp.status_code == 200

