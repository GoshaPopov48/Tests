import pytest
from conftest import api_client, get_user_id
from schemas.project_schemas import ProjectSchemas

@pytest.mark.parametrize(
    "name, shortName",
    [
        ("Test_no_project_id", " "),
        (" ", "pass"),
        (" ", " ")
        ]
)
def test_created_project_no_withoun_project_id(api_client, get_user_id, name, shortName):
    project_data = ProjectSchemas(
        name = name,
        shortName = shortName,
        leader= {"id": get_user_id}
    )
    
    response = api_client.post("/api/admin/projects",
    json = project_data.model_dump()
    )
    
    print("BODY", response.text)
    assert response.status_code == 400
    

