from framework.api.models.requests.project_schemas import ProjectSchemas, ProjectUpdateSchemas




class ProjectClient:
    def __init__(self, api_client):
        self.api_client = api_client
        
        
    def create_project(self, project_data: ProjectSchemas):
        return self.api_client.post(
            "/api/admin/projects",
            params = {"fields": "id,name,shortName"},
            json = project_data.model_dump()
        )
    
    def update_project(self, project_id, project_data: ProjectUpdateSchemas):
        return self.api_client.post(
            f"/api/admin/projects/{project_id}",
            params = {"fields": "id,name,shortName"},
            json = project_data.model_dump()
        )
        
    def delete_project(self, project_id):
        return self.api_client.delete(
            f"/api/admin/projects/{project_id}"
        )





