# In FastAPI, routes are defined in separate files and then included in the main app. This file defines the API routes for the application.

from fastapi import APIRouter

router = APIRouter() 

# Defining a route using a decortor. 
# When someone makes a GET request to /goals, run the function. 
@router.get("/goals") 
def get_goals() : 
    return [] # Place holder for now 

