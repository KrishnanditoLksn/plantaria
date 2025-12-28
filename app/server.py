import json
import traceback
from typing import Annotated, List, Optional, Union
import dotenv
from fastapi import Depends, FastAPI, HTTPException
from pydantic import BaseModel
from sqlalchemy import exists, select
from sqlalchemy.orm import Session


from app.database import Base, SessionLocal,engine
from app.model import plant
from app.model.plant import Plant
from app.request.plant_post_request import PlantRequest
from app.response.plant_detail_response import PlantResponse

app = FastAPI(
    title="Plants API", 
    description="Plants FastAPI Example", 
    version="0.1.0"
)


dotenv.load_dotenv()

Base.metadata.create_all(engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/")
def read_root():
    return {
        "Hello":"World"
    }


@app.get("/plants",response_model=List[PlantResponse],status_code=201)
async def get_all_plants(session:Session = Depends(get_db)):
    
    try:
        plant = session.query(Plant).all()
        return plant

    except Exception as e:
        raise HTTPException(
            status_code=404,
            detail={
                "status": "error",
                "error_type": type(e).__name__,
                "message": str(e),
                "traceback": traceback.format_exc()
            }
        )


@app.post("/plant/create")
def post_plant(plant:PlantRequest,db:Session = Depends(get_db)):
    try:
        is_present = db.scalars(select(exists().where(Plant.age == plant.age))).one()
        
        if is_present:
            return {
                "status":"error",
                "message":"Plant Already Exists"
            }
        else:
            plant = Plant(
                species = plant.species,
                age = plant.age,
                habitat = plant.habitat
            )
            db.add(plant)
            db.commit()
            return {
                "status":"success",
                "data":plant
            }
    except Exception as e :
        raise HTTPException(
            status_code=404,
            detail={
                "status": "error",
                "error_type": type(e).__name__,
                "message": str(e),
                "traceback": traceback.format_exc()
            }
        )


@app.get("/plant/{id}")
def get_plant_by_id(id:int , db:Session = Depends(get_db)):
    try:
        findPlant = db.get(Plant,id)
        
        if not findPlant:
            raise HTTPException(
                status_code=404, 
                detail="Plant not found"
            )
        return findPlant
        
    except Exception as e:
        raise HTTPException(
                status_code=404,
                detail={
                    "status": "error",
                    "error_type": type(e).__name__,
                    "message": str(e),
                    "traceback": traceback.format_exc()
                    }
        )