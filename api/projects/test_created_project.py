import pytest
from conftest import api_client, get_user_id
from schemas.project_schemas import ProjectSchemas






@pytest.mark.parametrize(
    "name, shortName",
    [
        ("Test_api_project_1", "TAP1"),
        ("Test_api_project_2", "TAP2"),
        ("Test_api_project_3", "TAP3"),
    ]
)
def test_created_project(api_client, get_user_id, name, shortName):
    project_data = ProjectSchemas(
        name = name,
        shortName = shortName,
        leader= {"id": get_user_id},
    )
    
    response = api_client.post("/api/admin/projects",
            params = {"fields": "id,name,shortName"},
            json = project_data.model_dump()
            )

    assert response.status_code == 200
    
    data = response.json()
    project_id = data["id"]
    
    try:
        assert data["id"]
        assert data["name"] == project_data.name
        assert data["shortName"] ==  project_data.shortName
        print(f"\nПроект был создан с id:{project_id}")
    finally:
        api_client.delete(f"/api/admin/projects/{project_id}")
        print(f"Проект {project_id} был удален")