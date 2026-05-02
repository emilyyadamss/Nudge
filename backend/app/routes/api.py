# In FastAPI, routes are defined in separate files and then included in the main app. This file defines the API routes for the application.

from fastapi import APIRouter
from app.models import Goal # Importing the Goal model to use in route definitions.

router = APIRouter() 

goals = []

# Defining a route using a decortor. 
# When someone makes a GET request to /goals, run the function. 
@router.get( "/goals" )
def get_goals() :
    return goals # Return the list of goals. In a real application, this would likely query a database.

# Set up a POST route to create a new goal.
@router.post( "/goals" )
def create_goal( goal: Goal ) : # The goal parameter is expected to be a Goal object, which FastAPI will automatically parse from the request body.
    goals.append( goal ) # Add the new goal to the list of goals.
    return goal # Return the newly created goal as a response.

# Set up a DELETE route to delete a goal by its ID.
@router.delete( "/goals/{goal_id}" )
def delete_goal( goal_id: int ) : # expected to be an integer, which FastAPI will parse from the URL path.
    global goals # Declare that we are modifying the global goals list.
    goals = [ goal for goal in goals if goal.id != goal_id ] # Create a new list of goals that excludes the one with the specified ID.
    return { "message": f"Goal with id {goal_id} deleted successfully." } # Return a message confirming deletion.
