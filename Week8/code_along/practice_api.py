# Import the requests library
import requests

# Create a class to encapsulate the API client. We are using a class to encapsulate the related methods and maintain state (base URL).
class ReqresAPIClient:
    # Define an init method that has a base URL as an optional parameter
    def __init__(self, base_url="https://reqres.in/api"):
        self.base_url = base_url
    
    # GET requests
    def get_users(self, page=1):
        response = requests.get(f"{self.base_url}/users?page={page}")
        if response.status_code == 200:
            return response.json()
        else:
            return None
        
    def get_user_by_id(self, user_id):
        response = requests.get(f"{self.base_url}/users/{user_id}")
        if response.status_code == 200:
            return response.json()['data']
        else:
            return None
    
    # POST Requests
    def create_user(self, name, job):
        data = {
            "name": name,
            "job": job
        }
        response = requests.post(f"{self.base_url}/users", json=data)
        if response.status_code == 201:
            return response.json()
        else:
            return None

client = ReqresAPIClient()

print("--- GET Requests ---")
users = client.get_users()

print(users)
print(users["data"][0]["first_name"])
specific_user = client.get_user_by_id(2)
print("Specific User:", specific_user)

# POST Demonstration
print("\n--- POST Requests ---")
new_user = client.create_user("Alice Smith", "Developer")
print("Created User:", new_user)