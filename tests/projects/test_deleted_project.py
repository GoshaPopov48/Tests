from framework.api.clients.response_client import ResponseClient





def test_deleted_project(project_client, created_project):
    
    response = project_client.delete_project(created_project)
    
    ResponseClient.check_response_success(response)