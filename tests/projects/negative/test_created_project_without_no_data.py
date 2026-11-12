import pytest
from framework.api.models.requests.project_schemas import ProjectSchemas

@pytest.mark.parametrize(
    "name, shortName",
    [
        ("Test_no_project_id", " "),
        (" ", "pass"),
        (" ", " ")
        ]
)
def test_created_project_no_without_project_id(project_client, get_user_id, name, shortName):
    project_data = ProjectSchemas(
        name = name,
        shortName = shortName,
        leader= {"id": get_user_id}
    )
    
    response = project_client.create_project(project_data)
    assert response.status_code == 400, response.text
    

