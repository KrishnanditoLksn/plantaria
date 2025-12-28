import traceback
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import exists, select
from sqlmodel import Session

from app.model.plant import Plant
from app.schemas.request.plant_post_request import PlantRequest
from app.db.database import get_db
from app.service.plant_service import add_plant


router = APIRouter()

@router.post("/add")
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