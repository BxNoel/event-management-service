from pydantic import BaseModel
from datetime import datetime
from typing import List

class OrganizationBase(BaseModel):
    name: str
    description: str

class Organization(OrganizationBase):
    id: int
    events: List["Event"] = []

    class Config:
        orm_mode = True


class EventBase(BaseModel):
    title: str
    description: str
    event_date: datetime
    location: str
    org_id: int

class Event(EventBase):
    id: int

    class Config:
        orm_mode = True
