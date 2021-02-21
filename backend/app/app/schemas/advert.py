from typing import Optional

from pydantic import BaseModel


# Shared properties
class AdvertBase(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    price: float = None
    location: str = None
    category: str = None
    inactive: bool = False

# Properties to receive on advert creation
class AdvertCreate(AdvertBase):
    title: str
    description: str
    price: float
    location: str
    category: str
    inactive: bool

# Properties to receive on advert update
class AdvertUpdate(AdvertBase):
    title: Optional[str]
    description: Optional[str]
    price: Optional[float]
    location: Optional[str]
    category: Optional[str]
    inactive: Optional[str]


# Properties shared by models stored in DB
class AdvertInDBBase(AdvertBase):
    id: int
    title: str
    description: str
    price: float
    location: str
    category: str
    inactive: bool
    owner_id: int

    class Config:
        orm_mode = True


# Properties to return to client
class Advert(AdvertInDBBase):
    pass


# Properties properties stored in DB
class AdvertInDB(AdvertInDBBase):
    pass
