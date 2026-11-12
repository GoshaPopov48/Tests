from framework.api.clients.users_client import UserClient
import pytest



@pytest.fixture
def user_client(api_client):
    return UserClient(api_client)