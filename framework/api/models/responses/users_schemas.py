from pydantic import BaseModel




class UsersResponse(BaseModel):
    id: str
    login: str
    fullName: str