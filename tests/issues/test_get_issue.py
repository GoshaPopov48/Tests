from framework.api.models.responses.issue_schemas import IssueResponse


def test_get_issue(issue_client, create_issue):
    response = issue_client.get_issue(create_issue)
    
    assert response.status_code == 200, response.text
    
    data = response.json()
    issue = IssueResponse.model_validate(data)

    assert issue.id == create_issue