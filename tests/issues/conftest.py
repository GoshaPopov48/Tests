import pytest
from framework.api.clients.issues_client import IssuesClient
from framework.api.models.requests.issue_schemas import IssuesSchemas
from framework.api.clients.response_client import ResponseClient


@pytest.fixture
def issue_client(api_client):
    return IssuesClient(api_client)

@pytest.fixture
def create_issue(issue_client, project_id):
    issue_data = IssuesSchemas(
        project={"id": project_id},
        summary ="Test Issue Auto",
        description="Description for auto create"
)
    response = issue_client.create_issue(issue_data)
    ResponseClient.check_response_success(response)
    
    issue_id = response.json()["id"]
    
    return issue_id
    