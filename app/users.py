from app.base_api import BaseAPI

class UsersAPI(BaseAPI):
    """
    CRUD methods inherited from BaseAPI:
        read: get all api data objects or get one object by id, for example api.read() or api.read(id=1)
        destroy: delete an api data object by id, for example api.destroy(id=1)
        create: create an api data object, the create function has the same arguments as the generate_payload function, for example api.create('arg1', 'arg2', 'arg3', other_arg='abc') if the generate_payload function header is: def generate_payload(foo, bar, baz, other_arg=None)
        update: update an api data object by id, the generate_payload function has all the arguments that can be updated, for example api.update(bar='updated_arg1', other_arg='updated_arg2') if the generate_payload function header is: def generate_payload(foo, bar, baz, other_arg=None)
    """

    def create_a_user_payload(self, name, job):
        return {
            "name": name,
            "job": job
        }

    def register_a_user_payload(self, email, password):
        return {
        "email": email,
        "password": password
    }   

users_api = UsersAPI()
