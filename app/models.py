from typing import Optional
from sqlmodel import SQLModel, Field

from app.schemas import TicketPriority, TicketStatus


class User(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    email: str = Field(index=True, unique=True)
    hashed_password: str


class Asset(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    category: str
    serial_number: str = Field(index=True, unique=True)
    status: str = Field(default="available")
    assigned_user_id: Optional[int] = Field(default=None, foreign_key="user.id")


class Ticket(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    title: str
    description: str
    status: TicketStatus = Field(default=TicketStatus.open)
    priority: TicketPriority = Field(default=TicketPriority.medium)
    user_id: int = Field(foreign_key="user.id")
    asset_id: Optional[int] = Field(default=None, foreign_key="asset.id")