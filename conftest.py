import pytest
import os
import uuid
from clients.youtrack_client import YouTrackClient
from playwright.sync_api import sync_playwright, expect
from tests.ui.pages.login_schemas import LoginPage
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
    
# Фикстура для авторизации теста UI
@pytest.fixture
def authenticated_page():
    with sync_playwright() as pl:
        browser = pl.chromium.launch(headless=False)
        page = browser.new_page()
        
        try:
            page.goto("http://localhost:8081/hub/auth/login")
            
            login_page = LoginPage(page)
            login_page.login(os.getenv("UI_USERNAME"), os.getenv("UI_PASSWORD"))
            
            expect(page).to_have_url("http://localhost:8081/dashboard")
            
            yield page
            
        finally:
            browser.close()