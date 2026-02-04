from pydantic import BaseModel
from typing import Optional

class UberBooking(BaseModel):
    pickup: Optional[str]
    drop: Optional[str]
    ride_type: Optional[str]

class AmazonOrder(BaseModel):
    product: Optional[str]
    quantity: Optional[int]
    address: Optional[str]

class BlinkitOrder(BaseModel):
    items: Optional[list]
    address: Optional[str]
