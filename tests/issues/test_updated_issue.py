import pytest
from framework.api.models.requests.issue_schemas import IssuesUpdatedSchemas
from framework.api.models.responses.issue_schemas import IssuesUpdatedSchemasResponse
from framework.api.clients.response_client import ResponseClient

@pytest.mark.parametrize(
    "summary, description",
    [
        ("Update summary for issue", "Update description for issue"),
        ("12412431", "fd234dxs"),
        ("ewsfr434", " ")
    ]
)
def test_updated_issue(issue_client, create_issue, summary, description):
    issue_data = IssuesUpdatedSchemas(
        summary = summary,
        description = description
    )
    response = issue_client.update_issue(create_issue, issue_data)
    
    data = ResponseClient.check_response_success(response)
    issue = IssuesUpdatedSchemasResponse.model_validate(data)
    
    assert issue.summary == issue_data.summary
    assert issue.description == issue_data.description