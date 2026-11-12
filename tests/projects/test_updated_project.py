import pytest
from framework.api.models.requests.project_schemas import ProjectUpdateSchemas
from framework.api.models.responses.project_schemas import ResponseUpdateSchemas

@pytest.mark.parametrize(
    "name, shortName",
    [
    ("Update_name_project_1", "UPD1"),
    ("Update_name_project_2", "UPD2"),
    ("Update_name_project_3", "UPD3")
    ]
)
def test_updated_project(project_client, created_project,  name, shortName):
    project_data = ProjectUpdateSchemas(
        name = name,
        shortName = shortName
    )
    
    response = project_client.update_project(created_project, project_data)
    
    assert response.status_code == 200, response.text
    
    data = response.json()
    
    project = ResponseUpdateSchemas.model_validate(data)
    
    assert project.name == project_data.name
    assert project.shortName == project_data.shortName
    