from pydantic import BaseModel   



class LeaderSchemas(BaseModel):
    id: str

class ProjectSchemas(BaseModel):
    name: str
    shortName: str
    leader: LeaderSchemas

class ProjectUpdateSchemas(BaseModel):
    name: str
    description: str
