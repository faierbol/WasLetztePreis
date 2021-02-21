from sqlalchemy.orm import Session
from random import randint

from app import crud
from app.schemas.advert import AdvertCreate, AdvertUpdate
from app.tests.utils.user import create_random_user
from app.tests.utils.utils import random_lower_string


def test_create_advert(db: Session) -> None:
    title = random_lower_string()
    description = random_lower_string()
    price = randint(1, 100)
    location = random_lower_string()
    category = random_lower_string()
    inactive = False
    advert_in = AdvertCreate(title=title,
                             description=description,
                             price=price,
                             location=location,
                             category=category,
                             inactive=inactive)
    user = create_random_user(db)
    advert = crud.advert.create_with_owner(db=db, obj_in=advert_in, owner_id=user.id)
    assert advert.title == title
    assert advert.description == description
    assert advert.price == price
    assert advert.location == location
    assert advert.category == category
    assert advert.inactive == inactive
    assert advert.owner_id == user.id


def test_get_advert(db: Session) -> None:
    title = random_lower_string()
    description = random_lower_string()
    price = randint(1, 100)
    location = random_lower_string()
    category = random_lower_string()
    inactive = False
    advert_in = AdvertCreate(title=title,
                             description=description,
                             price=price,
                             location=location,
                             category=category,
                             inactive=inactive)
    user = create_random_user(db)
    advert = crud.advert.create_with_owner(db=db, obj_in=advert_in, owner_id=user.id)
    stored_advert = crud.advert.get(db=db, id=advert.id)
    assert stored_advert
    assert advert.title == title
    assert advert.description == description
    assert advert.price == price
    assert advert.location == location
    assert advert.category == category
    assert advert.inactive == inactive
    assert advert.owner_id == user.id


def test_update_advert(db: Session) -> None:
    title = random_lower_string()
    description = random_lower_string()
    price = randint(1, 100)
    location = random_lower_string()
    category = random_lower_string()
    inactive = False
    advert_in = AdvertCreate(title=title,
                             description=description,
                             price=price,
                             location=location,
                             category=category,
                             inactive=inactive)
    user = create_random_user(db)
    advert = crud.advert.create_with_owner(db=db, obj_in=advert_in, owner_id=user.id)
    updated_description = random_lower_string()
    advert_update = AdvertUpdate(description=updated_description)
    advert_updated = crud.advert.update(db=db, db_obj=advert, obj_in=advert_update)
    assert advert.title == advert_updated.title
    assert advert.description == advert_updated.description
    assert advert.price == advert_updated.price
    assert advert.location == advert_updated.location
    assert advert.category == advert_updated.category
    assert advert.inactive == advert_updated.inactive
    assert advert.owner_id == advert_updated.owner_id
    assert advert.id == advert_updated.id

    assert advert_updated.description == updated_description


def test_delete_advert(db: Session) -> None:
    title = random_lower_string()
    description = random_lower_string()
    price = randint(1, 100)
    location = random_lower_string()
    category = random_lower_string()
    inactive = False
    advert_in = AdvertCreate(title=title,
                             description=description,
                             price=price,
                             location=location,
                             category=category,
                             inactive=inactive)
    user = create_random_user(db)
    advert = crud.advert.create_with_owner(db=db, obj_in=advert_in, owner_id=user.id)
    advert2 = crud.advert.remove(db=db, id=advert.id)
    advert_deleted = crud.advert.get(db=db, id=advert.id)
    assert advert_deleted is None
    assert advert2.id == advert.id
    assert advert2.title == title
    assert advert2.description == description
    assert advert2.price == price
    assert advert2.location == location
    assert advert2.category == category
    assert advert2.inactive == inactive
    assert advert2.owner_id == user.id
