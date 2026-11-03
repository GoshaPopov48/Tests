from conftest import api_client, created_issue_id


def test_get_issue(api_client, created_issue_id):
    response = api_client.get(f"/api/issues/{created_issue_id}",
    params = {"fields": "project,summary,description"})
    
    data = response.json()
    
    assert response.status_code == 200
    
    print(data)
    