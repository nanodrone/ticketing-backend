from typing import Optional
from sqlmodel import SQLModel

from enum import Enum
from typing import Optional
from sqlmodel import SQLModel


class UserCreate(SQLModel):
    name: str
    email: str


class UserRead(SQLModel):
    id: int
    name: str
    email: str


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
    priority: Optional[str] = "medium"
    user_id: int
    asset_id: Optional[int] = None


class TicketRead(SQLModel):
    id: int
    title: str
    description: str
    status: str
    priority: str
    user_id: int
    asset_id: Optional[int] = None

class TicketUpdate(SQLModel):
    status: Optional[str] = None
    priority: Optional[str] = None
    description: Optional[str] = None