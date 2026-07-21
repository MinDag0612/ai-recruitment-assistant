from datetime import datetime, UTC
from uuid import UUID, uuid4

from sqlmodel import SQLModel, Field
from sqlalchemy import DateTime

class BaseModel(SQLModel):
    id: UUID = Field(default_factory=uuid4, primary_key=True) # factory to get unique id
    created_at: datetime = Field(default_factory=lambda: datetime.now(UTC))