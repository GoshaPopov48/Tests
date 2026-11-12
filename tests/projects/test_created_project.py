import pytest
from framework.api.models.requests.project_schemas import ProjectSchemas
from framework.api.models.responses.project_schemas import ProjectResponse






@pytest.mark.parametrize(
    "name, shortName",
    [
        ("Test_api_project_1", "TAP1"),
        ("Test_api_project_2", "TAP2"),
        ("Test_api_project_3", "TAP3"),
    ]
)
def test_created_project(project_client, get_user_id, name, shortName):
    project_data = ProjectSchemas(
        name = name,
        shortName = shortName,
        leader= {"id": get_user_id},
    )
    
    response = project_client.create_project(project_data)
    
    assert response.status_code == 200, response.text
    
    data = response.json()
    
    project = ProjectResponse.model_validate(data)
    
    assert project.name == project_data.name
    assert project.shortName == project_data.shortName
    
    
    project_client.delete_project(project.id)
        