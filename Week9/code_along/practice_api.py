# start of code imported from last week
import requests

# Create a class to encapsulate the API client. We are using a class to encapsulate the related methods and maintain state (base URL).
class ReqresAPIClient:
    # Define an __init__ method that has a base URL as an optional parameter
    def __init__(self, base_url="https://reqres.in/api"):
        self.base_url = base_url
    
    # GET users requests. Show the get request in the browser first
    def get_users(self, page=1):
        # Make a GET request to the users endpoint and the specified page
        response = requests.get(f"{self.base_url}/users?page={page}")
        # Return the JSON response if the status code is 200. Otherwise, return None
        if response.status_code == 200:
            return response.json()
        else:
            return None
    
    # GET user by ID requests
    def get_user_by_id(self, user_id):
        # Make a GET request to the user endpoint with the specified user ID
        response = requests.get(f"{self.base_url}/users/{user_id}")
        # Return the JSON response if the status code is 200. Otherwise, return None
        if response.status_code == 200:
            return response.json()['data']
        else:
            return None
    
    # POST Requests
    # Create a new user with the specified name and job
    def create_user(self, name, job):
        # Create a dictionary with the name and job
        data = {
            "name": name,
            "job": job
        }
        # Make a POST request to the users endpoint with the data
        response = requests.post(f"{self.base_url}/users", data)
        # Return the JSON response if the status code is 201 (created). Otherwise, return None
        if response.status_code == 201:
            return response.json()
        else:
            return None
    # end of code imported from last week

    # Create an update_user method that updates the user with the specified ID
    def update_user(self, user_id, name, job):
        # Create a dictionary with the name and job
        data = {
            "name": name,
            "job": job
        }
        # Make a PUT request to the users endpoint with the data
        response = requests.put(f"{self.base_url}/users/{user_id}", data)
        # Return the JSON response if the status code is 200 (OK). Otherwise, return None
        if response.status_code == 200:
            return response.json()
        else:
            return None
    
    # Create a delete_user method that deletes the user with the specified ID
    def delete_user(self, user_id):
        # Make a DELETE request to the user endpoint with the specified user ID
        response = requests.delete(f"{self.base_url}/users/{user_id}")
        # Return True if the status code is 204 (No Content). Otherwise, return False
        if response.status_code == 204:
            return True
        else:
            return False

# Test outputs
client = ReqresAPIClient()

# PUT Demonstration
print("\n--- PUT Requests ---")
updated_user = client.update_user(2, "Alice Johnson", "Designer")
print("Updated User:")
print(updated_user)

# DELETE Demonstration
print("\n--- DELETE Requests ---")
deleted = client.delete_user(2)
print("User Deleted:", deleted)