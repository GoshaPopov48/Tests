from pydantic import BaseModel


class ProjectResponse(BaseModel):
    id: str
    name: str
    shortName: str

class ResponseUpdateSchemas(BaseModel):
    id: str
    name: str
    shortName: str
    
    