import pytest
from test_data.factories import (
generated_id_project, generated_name_project, 
generated_name_issues, generated_description_issue
)
from framework.api.clients.youtrack_client import YouTrackClient
from framework.api.clients.users_client import UserClient
from framework.api.clients.issues_client import IssuesClient
from framework.api.clients.projects_client import ProjectClient
from framework.api.models.responses.users_schemas import UsersResponse
from framework.api.models.requests.project_schemas import ProjectSchemas
from framework.api.models.responses.project_schemas import ProjectResponse
from framework.api.models.requests.issue_schemas import IssuesSchemas
from framework.api.models.responses.issue_schemas import IssueResponse


# Фикстура для подключения 
@pytest.fixture
def api_client():
    return YouTrackClient()

@pytest.fixture
def issue_client(api_client):
    return IssuesClient(api_client)

@pytest.fixture
def project_client(api_client):
    return ProjectClient(api_client)

@pytest.fixture
def user_client(api_client):
    return UserClient(api_client)



# Фикстура для получения user_id 
@pytest.fixture
def get_user_id(user_client):
    response = user_client.get_users() 
    data = response.json() 
    user = UsersResponse.model_validate(data)
    
    return  user.id

@pytest.fixture
def created_project(project_client, get_user_id):
    project_data = ProjectSchemas(
            name = generated_name_project("name"),
            shortName = generated_id_project("id"),
            leader= {"id": get_user_id},
        )
    
    
    response = project_client.create_project(project_data)
    
    assert response.status_code == 200, response.text
    
    data = response.json()
    
    project = ProjectResponse.model_validate(data)
    
    assert project.name == project_data.name
    assert project.shortName == project_data.shortName
    
    yield project.id
    
    project_client.delete_project(project.id)
    

@pytest.fixture
def project_id(project_client, get_user_id):
    project_data = ProjectSchemas(
        name = generated_name_project("test"),
        shortName = generated_id_project("test"),
        leader = {"id": get_user_id},
    )
    
    response = project_client.create_project(project_data)
    assert response.status_code == 200, response.text
    
    data = response.json()
    project = ProjectResponse.model_validate(data)
    yield project.id
    
    delete = project_client.delete_project(project.id)
    
    assert delete.status_code == 200, response.text


# Фикстура для создания задачи в проекте
@pytest.fixture 
def created_issue_id(issue_client, project_id):
    issue_data = IssuesSchemas(
        project = project_id,
        summary = generated_name_issues("test"),
        description = generated_description_issue("test")
    )
    
    response = issue_client.create_issue(issue_data)
    
    data = response.json()
    
    issue = IssueResponse.model_validate(data)
    
    yield issue.id
    
    delete_issue = issue_client.delete_issue(issue.id)
    
    assert delete_issue.status_code == 200, response.text
