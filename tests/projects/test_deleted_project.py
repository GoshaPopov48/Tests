def test_deleted_project(project_client, created_project):
    
    response = project_client.delete_project(created_project)
    
    assert response.status_code == 200
    