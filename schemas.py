from typing import Optional, List
from datetime import datetime
from pydantic import BaseModel, EmailStr


# ----------------------
# User Schemas
# -----------------------

class UserBase(BaseModel):
    username: str
    role: str  # Explicit role field here, e.g., "admin" or "customer"

class UserCreate(UserBase):
    password: str

class UserOut(UserBase):
    id: int

    class Config:
        from_attributes = True


# Token Data for JWT (used when decoding token)
class TokenData(BaseModel):
    username: Optional[str] = None
    role: Optional[str] = None  # Include role in token data for RBAC


# -----------------------
# Play Schemas
# -----------------------

class PlayBase(BaseModel):
    title: str
    genre: Optional[str] = None
    synopsis: Optional[str] = None
    duration: Optional[str] = None

class PlayCreate(PlayBase):
    pass

class PlayUpdate(BaseModel):
    title: Optional[str] = None
    genre: Optional[str] = None
    synopsis: Optional[str] = None
    duration: Optional[str] = None

class PlayOut(PlayBase):
    id: int

    class Config:
        from_attributes = True


# For search & pagination responses
class PlayListOut(BaseModel):
    total: int  # total records matching search
    items: List[PlayOut]


# -----------------------
# Actor Schemas
# -----------------------

class ActorBase(BaseModel):
    name: str
    gender: Optional[str] = None
    date_of_birth: Optional[datetime] = None

class ActorCreate(ActorBase):
    play_id: int

class ActorOut(ActorBase):
    id: int

    class Config:
        from_attributes = True


# -----------------------
# Director Schemas
# -----------------------

class DirectorBase(BaseModel):
    name: str

class DirectorCreate(DirectorBase):
    play_id: int

class DirectorOut(DirectorBase):
    id: int

    class Config:
        from_attributes = True


# -----------------------
# ShowTime Schemas
# -----------------------

class ShowTimeBase(BaseModel):
    date_and_time: datetime

class ShowTimeCreate(ShowTimeBase):
    play_id: int

class ShowTimeOut(ShowTimeBase):
    id: int

    class Config:
        from_attributes = True


# -----------------------
# Customer Schemas
# -----------------------

class CustomerBase(BaseModel):
    name: str
    phone_number: Optional[str] = None
    email: Optional[EmailStr] = None  # Add email for notifications
    address: str
class CustomerCreate(CustomerBase):
    pass

class CustomerOut(CustomerBase):
    id: int

    class Config:
        from_attributes = True


# -----------------------
# Ticket Schemas
# -----------------------

class TicketBase(BaseModel):
    seat_row_no: int
    seat_no: int
    ticket_no: Optional[str] = None
    price: float

class TicketCreate(TicketBase):
    showtime_id: int
    play_id: int
    customer_id: int

class TicketOut(TicketBase):
    showtime_id: int
    play_id: int
    customer_id: int

    class Config:
        from_attributes = True


# -----------------------
# Combined Relation Schemas (Optional Advanced Use)
# -----------------------

class PlayWithDetails(PlayOut):
    actors: List[ActorOut] = []
    directors: List[DirectorOut] = []
    showtimes: List[ShowTimeOut] = []

class CustomerWithTickets(CustomerOut):
    tickets: List[TicketOut] = []

class TicketWithRelations(TicketOut):
    play: PlayOut
    showtime: ShowTimeOut
    customer: CustomerOut
