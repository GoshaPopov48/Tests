def test_delete_issue(issue_client, create_issue):
    response = issue_client.delete_issue(create_issue)
    
    assert response.status_code == 200, response.text