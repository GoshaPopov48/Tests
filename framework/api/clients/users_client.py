




class UserClient:
    def __init__(self, api_client):
        self.api_client = api_client
    
    def get_users(self):
        return self.api_client.get(
            "/api/users/me",
            params={"fields": "id,login,fullName"}
        )
    