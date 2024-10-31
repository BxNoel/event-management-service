from fastapi import FastAPI, Depends, Request, HTTPException
from sqlalchemy.orm import Session

import logging
import sys


from app import models
from app import schemas
from typing import List 
from app.database import engine
from .dependencies import get_db

from starlette.middleware.base import BaseHTTPMiddleware
import time
from . import models, schemas, database, dependencies



app = FastAPI()

# Configure the logger to output to stderr
logging.basicConfig(
    filename="app.log",                # Log output file
    level=logging.INFO,                 # Logging level
    format="%(asctime)s - %(message)s", # Log format
    datefmt="%Y-%m-%d %H:%M:%S"
)
logger = logging.getLogger(__name__)
logger = logging.getLogger(__name__)

models.Base.metadata.create_all(bind=engine)
class LoggingMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        # Log the request details
        request_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        logger.info(f"Incoming request: {request.method} {request.url.path}")

        # Process the request and get the response
        response = await call_next(request)

        # Log the response details
        response_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        logger.info(f"Completed response: {response.status_code} {request.url.path}")

        return response

# Add the middleware to the FastAPI app
app.add_middleware(LoggingMiddleware)

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


@app.get("/events/search", response_model=List[schemas.Event])
def search_events(search_params: schemas.EventSearch = Depends(), db: Session = Depends(dependencies.get_db)):
    return database.search_events(db, search_params)

# Sub-resource functions
def validate_event(event_id: int, db: Session):
    # Check if the event exists and is valid
    event = db.query(models.Event).filter(models.Event.event_id == event_id).first()
    if not event:
        return False
    return True

def reserve_calendar_slot(event_id: int, db: Session):
    # Reserve a time slot on the calendar for the event
    # Let's assume it creates an entry in the calendar_entries table
    try:
        new_entry = models.CalendarEntry(event_id=event_id, calendar_date="2024-10-30 10:00:00")
        db.add(new_entry)
        db.commit()
        db.refresh(new_entry)
        return True
    except Exception as e:
        print("Error reserving calendar slot:", e)
        db.rollback()
        return False

def send_confirmation(event_id: int):
    # Send confirmation (this could be a placeholder function)
    print(f"Confirmation sent for event {event_id}")
    return True

# Main endpoint to coordinate the synchronous calls
@app.post("/events/schedule/{event_id}")
def schedule_event(event_id: int, db: Session = Depends(dependencies.get_db)):
    # Step 1: Validate Event
    if not validate_event(event_id, db):
        raise HTTPException(status_code=404, detail="Event not found or invalid")

    # Step 2: Reserve Calendar Slot
    if not reserve_calendar_slot(event_id, db):
        raise HTTPException(status_code=500, detail="Failed to reserve calendar slot")

    # Step 3: Send Confirmation
    if not send_confirmation(event_id):
        raise HTTPException(status_code=500, detail="Failed to send confirmation")

    return {"message": "Event scheduled successfully"}