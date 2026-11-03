import pytest
from conftest import api_client, created_issue_id
from schemas.issue_schemas import IssuesUpdatedSchemas

@pytest.mark.parametrize(
    "summary, description",
    [
        ("Update summary for issue", "Update description for issue"),
        ("12412431", "fd234dxs"),
        ("ewsfr434", " ")
    ]
)
def test_updated_issue(api_client, created_issue_id, summary, description):
    issue_data = IssuesUpdatedSchemas(
        summary = summary,
        description = description
    )
    response = api_client.post(f"/api/issues/{created_issue_id}",
    params = {"fields": "id,summary"},
    json = issue_data.model_dump()
    )
    
    assert response.status_code == 200
    
    data = response.json()
    
    assert data["id"] == created_issue_id
    assert data["summary"] == issue_data.summary