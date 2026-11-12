from framework.api.models.responses.users_schemas import UsersResponse


def test_auth(user_client):
    response = user_client.get_users()
    
    assert response.status_code == 200, response.text 
    data = response.json()
    user = UsersResponse.model_validate(data)
    
    assert user.login
    assert user.fullName
    assert user.id