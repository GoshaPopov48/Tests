import pytest
from conftest import api_client, created_issue_id
from schemas.issue_schemas import IssuesSchemas

@pytest.mark.parametrize(
    "summary, description",
    [
        ("Update summary for issue", "Update description for issue"),
        ("12412431", "fd234dxs"),
        ("ewsfr434", " ")
    ]
)
def test_update_issue_non_authorization(api_client, project_id, summary, description):
    issue_data = IssuesSchemas(
                project = {"id": project_id},
                summary = summary,
                description = description
            )
    
    response = api_client.post(f"/api/issues/{project_id}",
    params = {"fields": "id,summary"},
    headers = {"Authorization": ""},
    json = issue_data.model_dump()
    )
    
    print("BODY", response.text)
    assert response.status_code == 401