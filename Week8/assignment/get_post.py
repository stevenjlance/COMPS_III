import requests

class JSONPlaceholder:
    def __init__(self, base_url):
        self.base_url = base_url
    
    def get_request(self):
        response = requests.get(self.base_url)
        data = {
            "status_code": response.status_code,
            "headers": response.headers,
            # First 500 characters of the content
            "content": response.content[:500]
        }
        return data
    
    def get_request_by_userid(self, user_id):
        response = requests.get(f'{self.base_url}?userId={user_id}')
        data = {
            "status_code": response.status_code,
            "headers": response.headers,
            # First 500 characters of the content
            "content": response.content[:500]
        }
        return data
    
    def post_request(self, data):
        response = requests.post(self.base_url, data=data)
        data = {
            "status_code": response.status_code,
            "headers": response.headers,
            # First 500 characters of the content
            "content": response.content[:500]
        }
        return data