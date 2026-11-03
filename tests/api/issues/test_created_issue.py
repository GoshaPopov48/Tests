import pytest
from conftest import api_client, project_id
from schemas.issue_schemas import IssuesSchemas


@pytest.mark.parametrize(
    "summary, description",
    [
        ("it's name is for Test_1", "Is description created in the the test api task_2"),
        ("2143234", "325435r43 "),
        ("def43", " ")

        
    ]
)
def test_created_issue(api_client, project_id, summary, description):
    issue_data = IssuesSchemas(
        project = {"id": project_id},
        summary = summary,
        description = description
    )
    
    response = api_client.post("/api/issues",
        params = {"fields": "id,type,summary,project(id,name)"},
        json = issue_data.model_dump()
        )
    

    data = response.json()

    assert data["summary"] == issue_data.summary
    assert data["project"]["id"] == project_id
    assert response.status_code == 200
