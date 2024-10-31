from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey, TIMESTAMP
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from .database import Base

# Organization Model
class Organization(Base):
    __tablename__ = "organizations"

    org_id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    name = Column(String(100), nullable=False)
    description = Column(Text)
    created_at = Column(TIMESTAMP, server_default=func.now())

    # Relationship to Event
    events = relationship("Event", back_populates="organization", cascade="all, delete")

# Event Model
class Event(Base):
    __tablename__ = "events"

    event_id = Column(Integer, primary_key=True, index=True)
    org_id = Column(Integer, ForeignKey("organizations.org_id"), nullable=False)
    title = Column(String(255), nullable=False)
    description = Column(Text)
    event_date = Column(DateTime, nullable=False)
    location = Column(String(255), nullable=False)
    created_at = Column(DateTime)
    updated_at = Column(DateTime)
    # Relationship to Organization
    organization = relationship("Organization", back_populates="events")
    
class CalendarEntry(Base):
    __tablename__ = "calendar_entries"

    entry_id = Column(Integer, primary_key=True, index=True)
    event_id = Column(Integer, ForeignKey("events.event_id"), nullable=False)
    calendar_date = Column(DateTime, nullable=False)
    reminder_time = Column(DateTime, nullable=True)