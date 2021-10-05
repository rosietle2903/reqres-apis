import json

import requests

class BaseAPI:

    def get(self, path, payload=None, params=None):
            try:
                full_url = self.end_point_url(path)
                response = requests.get(full_url, json=payload, params=params, verify=False)
                return response
            except Exception as e:
                print(f"EXCEPTION GET {path}. {e}")
                return None

    def post(self, path, payload=None, data=None, headers=None, files=None):
            try:
                full_url = self.end_point_url(path)
                response = requests.post(full_url, headers=headers, json=payload, data=data, files=files, verify=False)
                return response
            except Exception as e:
                print(f"EXCEPTION POST {path}. {e}")
                return None

    def put(self, path, payload=None):
            try:
                full_url = self.end_point_url(path)
                response = requests.put(full_url, json=payload, verify=False)
                return response
            except Exception as e:
                print(f"EXCEPTION PUT {path}. {e}")
                return None

    def delete(self, path):
            try:
                full_url = self.end_point_url(path)
                response = requests.delete(full_url, verify=False)
                return response
            except Exception as e:
                print(f"EXCEPTION DELETE {path}. {e}")
                return None

    def end_point_url(self, path=''):
        return f"https://reqres.in{path}"
    
    


