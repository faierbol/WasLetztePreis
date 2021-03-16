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
    rating: int = None
    image_link: str = None

# Properties to receive on advert creation
class AdvertCreate(AdvertBase):
    title: str
    description: str
    price: float
    location: str
    category: str
    inactive: bool
    rating: int
    image_link: str

# Properties to receive on advert update
class AdvertUpdate(AdvertBase):
    title: Optional[str]
    description: Optional[str]
    price: Optional[float]
    location: Optional[str]
    category: Optional[str]
    inactive: Optional[str]
    rating: Optional[int]
    image_link: Optional[str]


# Properties shared by models stored in DB
class AdvertInDBBase(AdvertBase):
    id: int
    title: str
    description: str
    price: float
    location: str
    category: str
    inactive: bool
    rating: int
    image_link: str
    owner_id: int

    class Config:
        orm_mode = True


# Properties to return to client
class Advert(AdvertInDBBase):
    pass


# Properties properties stored in DB
class AdvertInDB(AdvertInDBBase):
    pass
