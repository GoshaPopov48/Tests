import pytest
from framework.api.models.requests.issue_schemas import IssuesSchemas
from framework.api.models.responses.issue_schemas import IssueResponse


@pytest.mark.parametrize(
    "summary, description",
    [
        ("it's name is for Test_1", "Is description created in the the test api task_2"),
        ("2143234", "325435r43 "),
        ("def43", " ")

        
    ]
)
def test_created_issue(issue_client, project_id, summary, description):
    issue_data = IssuesSchemas(
        project = {"id": project_id},
        summary = summary,
        description = description
    )
    
    response = issue_client.create_issue(issue_data)
    
    assert response.status_code == 200, response.text
    
    data = response.json()
    issue = IssueResponse.model_validate(data)
    
    assert issue.summary == issue_data.summary
    assert issue.project.id == project_id
