from fastapi import Depends
from sqlmodel import Session

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
    db.get(
        Plant,
        id
    )

def get_plants(db:Session = Depends(get_db)):
    db.query(Plant).all()