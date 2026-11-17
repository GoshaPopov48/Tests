from framework.api.clients.response_client import ResponseClient




def test_delete_issue(issue_client, create_issue):
    response = issue_client.delete_issue(create_issue)
    
    ResponseClient.check_response_success(response)