from pydantic import BaseModel


class ProjectResponse(BaseModel):
    id: str
    name: str


class IssueResponse(BaseModel):
    id: str
    summary: str
    project: ProjectResponse
    
    
class IssuesUpdatedSchemasResponse(BaseModel):
    id: str
    summary: str
    description: str
    