from pydantic import BaseModel



class ProjectSchemas(BaseModel):
    id: str

class IssuesSchemas(BaseModel):
    project: ProjectSchemas
    summary: str
    description: str

class IssuesUpdatedSchemas(BaseModel):
    summary: str
    description: str
    
