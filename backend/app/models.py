# Holds data model definitions for the application. Separate from the routes. 

from pydantic import BaseModel

# Shape and values of a goal object. Pydantic is used to validate and serialize data in FastAPI.
class Goal(BaseModel):
    id: int
    name: str
    category: str
    priority: int
    hours_logged: float
    description: str
    indefinite: bool
    is_active: bool 

