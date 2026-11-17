from framework.api.models.responses.issue_schemas import IssueResponse
from framework.api.clients.response_client import ResponseClient

def test_get_issue(issue_client, create_issue):
    response = issue_client.get_issue(create_issue)
    
    data = ResponseClient.check_response_success(response)
    issue = IssueResponse.model_validate(data)

    assert issue.id == create_issue