from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session

from app import models
from app import schemas
from typing import List  # Import List
from app.database import engine
from .dependencies import get_db

app = FastAPI()

models.Base.metadata.create_all(bind=engine)

@app.get("/")
def read_root():
    return {"message": "Hello, FastAPI!"}

@app.get("/organizations/", response_model=List[schemas.Organization])
def read_organizations(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return db.query(models.Organization).offset(skip).limit(limit).all()

@app.get("/events/", response_model=List[schemas.Event])
def read_events(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return db.query(models.Event).offset(skip).limit(limit).all()