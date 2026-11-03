import pytest
from conftest import api_client, project_id
from schemas.project_schemas import ProjectUpdateSchemas


@pytest.mark.parametrize(
    "name, description",
    [
    ("Update_name_project_1", "Updated_1!"),
    ("Update_name_project_2", "Updated_2!"),
    ("Update_name_project_3", "Updated_3!")
    ]
)
def test_updated_project(api_client, project_id, name, description):
    project_data = ProjectUpdateSchemas(
        name = name,
        description = description
    )
    response = api_client.post(f"/api/admin/projects/{project_id}",
        params = {"fields": "id,name,shortName"},
        json = project_data.model_dump()
        )
    
    data = response.json()
    
    assert data["name"] == project_data.name
    assert response.status_code == 200
    print("Название проекта успешно обновлено!")
    