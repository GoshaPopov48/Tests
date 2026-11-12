from framework.api.models.requests.issue_schemas import IssuesSchemas, IssuesUpdatedSchemas




class IssuesClient:
    
    def __init__(self, api_client):
        self.api_client = api_client
        
    def create_issue(self, issue_data: IssuesSchemas):
        return self.api_client.post(
            "/api/issues",
            params = {"fields": "id,type,summary,project(id,name)"},
            json = issue_data.model_dump()
        )
    
    def get_issue(self, issue_id):
        return self.api_client.get(f"/api/issues/{issue_id}",
            params={"fields": "id,summary,description,project(id,name)"}
        )
        
    def update_issue(self, issue_id, issue_data: IssuesUpdatedSchemas, **kwargs):
        return self.api_client.post(f"/api/issues/{issue_id}",
            params={"fields": "id,summary,description,project(id,name)"},
            json = issue_data.model_dump(),
            **kwargs
            )
        
    def delete_issue(self, issues_id):
        return self.api_client.delete(
            f"/api/issues/{issues_id}"
        )