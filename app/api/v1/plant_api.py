import traceback
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import exists, select
from sqlmodel import Session

from app.model.plant import Plant
from app.schemas.request.plant_post_request import PlantRequest
from app.db.database import get_db
from app.service.plant_service import add_plant, get_all_plants, get_plant_id


router = APIRouter(
    prefix='/api/v1'
)

@router.post("/plant/add")
def post_plant(plant:PlantRequest , db:Session = Depends(get_db)):
        try:
            is_present = db.scalars(
                select(
                    exists().where(Plant.species == plant.species)
                    )
            ).one()
        
            if is_present:
                return {
                    "status":"error",
                    "message":"Plant Already Exists"
                }
            else:
                add_plant(
                    plant,db
                )
                return {
                    "status":"success"
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

@router.get("/plant/{id}")
def get_plant_by_id(id:int , db:Session = Depends(get_db)):
    try:
        plantFound = get_plant_id(
            id,
            db
        )
        return plantFound
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

@router.get("/plants",response_model=list[PlantRequest])
def get_plants(db:Session = Depends(get_db)):
    try:
        all_plants = get_all_plants(db)
        return  all_plants
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