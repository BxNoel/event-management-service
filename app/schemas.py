from pydantic import BaseModel
from datetime import datetime
from typing import List, Optional

class OrganizationBase(BaseModel):
    name: str
    description: Optional[str] = None

class OrganizationCreate(OrganizationBase):
    pass

class Organization(OrganizationBase):
    org_id: int
    created_at: datetime

    class Config:
        orm_mode = True
