from framework.api.models.responses.users_schemas import UsersResponse
from framework.api.clients.response_client import ResponseClient

def test_auth(user_client):
    response = user_client.get_users()
    
    ResponseClient.check_response_success(response)
    data = response.json()
    user = UsersResponse.model_validate(data)
    
    assert user.login
    assert user.fullName
    assert user.id