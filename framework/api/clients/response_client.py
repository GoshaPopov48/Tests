import pytest



class ResponseClient:
    
    @staticmethod
    def check_response_success(response):
        assert response.status_code == 200, response.text
        
        if not response.content:
            return None

        return response.json()
    
    @staticmethod
    def check_response_error(response):
        assert response.status_code == 400, response.text
        
        if not response.content:
            return None

        return response.json()
    
    @staticmethod
    def check_response_error_forbidden(response):
        assert response.status_code == 401, response.text
        
        if not response.content:
            return None

        return response.json()