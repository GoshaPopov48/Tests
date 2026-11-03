from conftest import api_client, created_issue_id


def test_delete_issue(api_client, created_issue_id):
    response = api_client.delete(f"/api/issues/{created_issue_id}")
    
    assert response.status_code == 200