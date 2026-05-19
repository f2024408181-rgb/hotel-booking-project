from pydantic import BaseModel
from typing import Optional


class BookingModel(BaseModel):
    full_name: str
    email: str
    phone: str
    check_in: str
    check_out: str
    room_type: str
    guests: Optional[int] = None
    requests: Optional[str] = None
