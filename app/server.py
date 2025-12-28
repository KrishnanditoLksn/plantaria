import json
import traceback
from typing import Annotated, List, Optional, Union
import dotenv
from fastapi import Depends, FastAPI, HTTPException
from pydantic import BaseModel
from sqlalchemy import exists, select
from sqlalchemy.orm import Session
from app.api.v1 import plant_api

from app.db.database import Base, SessionLocal,engine, get_db
from app.model import plant
from app.model.plant import Plant
from app.schemas.request.plant_post_request import PlantRequest
from app.schemas.response.plant_detail_response import PlantResponse

app = FastAPI(
    title="Plants API", 
    description="Plants FastAPI Example", 
    version="0.1.0"
)


dotenv.load_dotenv()

Base.metadata.create_all(engine)


# def get_db():
#     db = SessionLocal()
#     try:
#         yield db
#     finally:
#         db.close()


@app.get("/")
def read_root():
    return {
        "Hello":"World"
    }


@app.get("/plants",response_model=List[PlantResponse],status_code=201)
def get_all_plants(session:Session = Depends(get_db)):
    
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

app.include_router(
    plant_api.router , prefix="/api/v1/plant"
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