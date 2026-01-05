from fastapi import Depends
from sqlmodel import Session , select

from app.model.plant import Plant
from app.schemas.request.plant_post_request import PlantRequest
from app.db.database import get_db


def add_plant(plant:PlantRequest,db:Session = Depends(get_db)):
    plant = Plant(
                species = plant.species,
                age = plant.age,
                habitat = plant.habitat
            )
    db.add(plant)
    db.commit()

def get_plant_id(id:int , db:Session = Depends(get_db)):
    return db.get(
        Plant,
        id
    )

def get_all_plants(db: Session):
    stmt = select(Plant)
    return db.scalars(
        stmt
    ).all()