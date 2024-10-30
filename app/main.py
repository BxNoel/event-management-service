from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
import time
import logging

from app import models
from app import schemas
from typing import List 
from app.database import engine
from app.dependencies import get_db 
from sqlalchemy.exc import OperationalError 


app = FastAPI()

# Wait for the database to be ready
max_retries = 10
for attempt in range(max_retries):
    try:
        # Try to connect to the database
        with engine.connect() as conn:
            break  # If successful, exit the loop
    except OperationalError:
        print(f"Database connection failed. Retrying in 5 seconds... (Attempt {attempt + 1}/{max_retries})")
        time.sleep(5)
else:
    print("Failed to connect to the database after several attempts.")
    sys.exit(1)  # Exit the application if the database is not ready

# Create tables after ensuring the database is ready
models.Base.metadata.create_all(bind=engine)


@app.get("/")
def read_root():
    return {"message": "Hello, FastAPI!"}

@app.get("/organizations/", response_model=List[schemas.Organization])
def read_organizations(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    organizations = db.query(models.Organization).offset(skip).limit(limit).all()
    return organizations

@app.get("/events/", response_model=List[schemas.Event])
def read_events(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return db.query(models.Event).offset(skip).limit(limit).all()
