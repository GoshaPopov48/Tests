import pytest
from tests.conftest import api_client, project_id
from framework.api.models.requests.issue_schemas import IssuesSchemas

@pytest.mark.parametrize(
    "summary, description",
    [
        (" ", "Is description created in the the test api task")
    ]
)
def test_created_without_name_issue(issue_client, project_id, summary, description):
    issue_data = IssuesSchemas(
            project = {"id": project_id},
            summary = summary,
            description = description
        )
    
    response = issue_client.create_issue(issue_data)
    
    
    print("BODY:", response.text)
    
    assert response.status_code == 400
    