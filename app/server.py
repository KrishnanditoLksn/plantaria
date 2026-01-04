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


@app.get("/")
def read_root():
    return {
        "Hello":"World"
    }
    
app.include_router(
    plant_api.router
)