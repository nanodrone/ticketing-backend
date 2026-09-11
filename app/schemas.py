from typing import Optional
from sqlmodel import SQLModel

from enum import Enum
from typing import Optional
from sqlmodel import SQLModel

class TicketStatus(str, Enum):
    open = "open"
    in_progress = "in_progress"
    closed = "closed"

class TicketPriority(str, Enum):
    low = "low"
    medium = "medium"
    high = "high"

class UserCreate(SQLModel):
    name: str
    email: str
    password: str


class UserRead(SQLModel):
    id: int
    name: str
    email: str

class Token(SQLModel):
    access_token: str
    token_type: str

class TokenData(SQLModel):
    email: Optional[str] = None

class AssetCreate(SQLModel):
    name: str
    category: str
    serial_number: str
    status: Optional[str] = "available"
    assigned_user_id: Optional[int] = None


class AssetRead(SQLModel):
    id: int
    name: str
    category: str
    serial_number: str
    status: str
    assigned_user_id: Optional[int] = None


class TicketCreate(SQLModel):
    title: str
    description: str
    priority: TicketPriority = TicketPriority.medium
    user_id: int
    asset_id: Optional[int] = None


class TicketRead(SQLModel):
    id: int
    title: str
    description: str
    status: TicketStatus
    priority: TicketPriority
    user_id: int
    asset_id: Optional[int] = None

class TicketUpdate(SQLModel):
    status: Optional[TicketStatus] = None
    priority: Optional[TicketPriority] = None
    description: Optional[str] = None