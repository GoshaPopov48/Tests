import pytest
from framework.api.models.requests.issue_schemas import IssuesUpdatedSchemas
from framework.api.clients.response_client import ResponseClient


@pytest.mark.parametrize(
    "summary, description",
    [
        ("Update summary for issue", "Update description for issue"),
        ("12412431", "fd234dxs"),
        ("ewsfr434", " ")
    ]
)
def test_update_issue_non_authorization(issue_client, create_issue, summary, description):
    issue_data = IssuesUpdatedSchemas(
        summary=summary,
        description=description
    )

    response = issue_client.update_issue(
        create_issue,
        issue_data,
        headers={"Authorization": ""}
    )

    print("BODY:", response.text)

    ResponseClient.check_response_error_forbidden(response)
