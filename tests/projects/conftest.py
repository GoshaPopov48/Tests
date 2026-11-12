# Фикстура для получения  создания и получения id проекта 
import pytest
from framework.api.clients.projects_client import ProjectClient
from framework.api.models.requests.project_schemas import ProjectSchemas
from framework.api.models.responses.project_schemas import ProjectResponse
from test_data.factories import generated_id_project, generated_name_project

@pytest.fixture
def project_client(api_client):
    return ProjectClient(api_client)


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
    
    