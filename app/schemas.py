from pydantic import BaseModel, Field
from typing import List, Optional
from datetime import datetime

# Event Schema for response
class EventBase(BaseModel):
    title: str
    description: Optional[str]
    event_date: datetime
    location: str

class Event(EventBase):
    id: int = Field(..., alias='event_id')  # Use alias to map event_id to id

    class Config:
        orm_mode = True
        allow_population_by_field_name = True  # This allows access via 'id' or 'event_id'

# Organization Schema for response
class OrganizationBase(BaseModel):
    name: str
    description: Optional[str] = None

class Organization(OrganizationBase):
    id: int = Field(..., alias='org_id')  # Use alias to map org_id to id
    events: List[Event] = []

    class Config:
        orm_mode = True
        allow_population_by_field_name = True  # This allows access via 'id' or 'org_id'