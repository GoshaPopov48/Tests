import pytest
from conftest import api_client, project_id
from schemas.issue_schemas import IssuesSchemas


@pytest.mark.parametrize(
    "summary, description",
    [
        (" ", "Is description created in the the test api task")
    ]
)
def test_created_without_name_issue(api_client, project_id, summary, description):
    issue_data = IssuesSchemas(
            project = {"id": project_id},
            summary = summary,
            description = description
        )
    
    response = api_client.post("/api/issues",
        params = {"fields": "id,type,summary,project(id,name)"},
        json = issue_data.model_dump()
        )
    
    print("BODY:", response.text)
    
    assert response.status_code == 400
    