# File to create the app object and attach routes to it 

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes import api 

app = FastAPI() # Object that FastAPI uses to keep track of all routes, middleware, and settings. 

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],  # Allow only from this origin
    allow_methods=["*"],  # Allow all HTTP methods
    allow_headers=["*"],  # Allow all headers
)

app.include_router(api.router) # Include the API router that defined in routes/api.py