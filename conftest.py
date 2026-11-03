import pytest
import os
import uuid
from clients.youtrack_client import YouTrackClient
from dotenv import load_dotenv

load_dotenv()

# Фикстура для подключения 
@pytest.fixture
def api_client():
    return YouTrackClient()

# Фикстура для получения user_id 
@pytest.fixture
def get_user_id(api_client):
    response = api_client.get(
        "/api/users/me",
        params={"fields": "id"}
    )
    data = response.json()
    user_id = data["id"]
    
    return  user_id

# Фикстура для получения  создания и получения id проекта 
@pytest.fixture
def project_id(api_client, get_user_id):
    suffix = uuid.uuid4().hex[:6].upper()
    response = api_client.post(
        "/api/admin/projects",
        json={
            "name": f"Test{suffix}",
            "shortName": f"P{suffix}",
            "leader": {
                "id": get_user_id
            }
        }
    )
    
    data = response.json()
    project_id = data["id"]
    yield project_id
    
    # Удаляем проект после его обновления
    api_client.delete(f"/api/admin/projects/{data["id"]}")

# Фикстура для создания задачи в проекте
@pytest.fixture 
def created_issue_id(api_client, project_id):
    response = api_client.post("/api/issues",
    params = {"fields": "id,summary"},
    json = {
                "project": {"id": project_id},
                "summary": "it's name is for Test",
                "description": "Is description created in the the test api task"
            })
    
    data = response.json()
    
    
    return data["id"]