from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy.orm import Session
from . import models, schemas


# Database URL for MySQL (adjust your actual connection string accordingly)
SQLALCHEMY_DATABASE_URL = "mysql+pymysql://root:password@localhost:3306/event_management_service"

# Create the SQLAlchemy engine (no need for connect_args)
engine = create_engine(SQLALCHEMY_DATABASE_URL)

# Create a session local to interact with the database
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base class for declarative models
Base = declarative_base()

def search_events(db: Session, search_params: schemas.EventSearch):
    query = db.query(models.Event)
    
    if search_params.title:
        query = query.filter(models.Event.title.ilike(f"%{search_params.title}%"))
    if search_params.event_date:
        query = query.filter(models.Event.event_date == search_params.event_date)
    if search_params.location:
        query = query.filter(models.Event.location.ilike(f"%{search_params.location}%"))
    
    return query.all()
