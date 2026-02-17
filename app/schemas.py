from uuid import UUID
from pydantic import BaseModel, ConfigDict

class UserCreate(BaseModel):
    email: str
    name: str
    age: int | None = None

class UserResponse(BaseModel):
    id: UUID
    email: str
    name: str
    age: int | None = None
    
    model_config = ConfigDict(from_attributes=True)

class OrderCreate(BaseModel):
    user_id: UUID
    product_name: str
    total: float

class OrderResponse(BaseModel):
    id: UUID
    user_id: UUID
    product_name: str
    total: float
    
    model_config = ConfigDict(from_attributes=True)