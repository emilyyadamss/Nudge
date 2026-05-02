# In FastAPI, routes are defined in separate files and then included in the main app. This file defines the API routes for the application.

from fastapi import APIRouter
from app.models import Goal # Importing the Goal model to use in route definitions.

router = APIRouter() 

# Defining a route using a decortor. 
# When someone makes a GET request to /goals, run the function. 
@router.get("/goals") 
def get_goals() : 
    goal = Goal( id=1, name="Japanese", category="Language", priority=1, hours_logged=0.0, description="Learn Japanese to fluency", indefinite=True, is_active=True)
    return [goal] # Place holder for now 


