import requests

class JSONPlaceholder:
    def __init__(self, base_url):
        self.base_url = base_url
    
    def update_user(self, userId, title, body):
        data = {
            "title": title,
            "body": body
        }
        response = requests.put(f'{self.base_url}/{userId}', data)

        data = {
            "status_code": response.status_code,
            "headers": response.headers,
            "content": response.content[:500]
        }
        return data

    def delete_user(self, userId):
        response = requests.delete(f'{self.base_url}/{userId}')
        data = {
            "status_code": response.status_code,
        }
        return data

base_url = "https://jsonplaceholder.typicode.com/posts"
json_placeholder = JSONPlaceholder(base_url)
data = json_placeholder.update_user(3, "My test", "Testing for user 3")
print(data)
print(json_placeholder.delete_user(5))
print(json_placeholder.delete_user(42))
print(json_placeholder.delete_user(90))