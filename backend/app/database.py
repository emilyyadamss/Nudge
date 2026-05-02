from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase

# SQLAlchemy's connection string format. ./nudge.db is the file it'll create in the working directory
DATABASE_URL = "sqlite:///./nudge.db" # Define the database URL. 

# The core connection object. Set to false because FastAPI can handle more than one thread. 
engine = create_engine( DATABASE_URL, connect_args={ "check_same_thread": False } )

# A temp workspace for a set of database ops. 
SessionLocal = sessionmaker( bind=engine )

# SQLAlchemy model that the class inherits. 
class Base( DeclarativeBase ) : 
    pass 