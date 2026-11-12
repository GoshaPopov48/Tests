import requests
from config.settings import Settings

class YouTrackClient():

    def __init__(self):
        
        self.base_url = Settings.BASE_URL
        token =  Settings.API_TOKEN
        
        assert token, "API_TOKEN не найден"
    
        self.session = requests.Session()
    
        self.session.headers.update({
            "Authorization": f"Bearer {token}",
            "Accept": "application/json"
        })
    

    def get(self, endpoint, **kwargs):
        return self.session.get(
            f"{self.base_url}{endpoint}",
            **kwargs
        )
    
    def post(self, endpoint, **kwargs):
        return self.session.post(
            f"{self.base_url}{endpoint}", 
            **kwargs
        )
    
    def delete(self, endpoint, **kwargs):
        return self.session.delete(
            f"{self.base_url}{endpoint}", 
            **kwargs
        )
