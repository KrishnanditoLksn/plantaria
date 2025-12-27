import json
from typing import Union
import dotenv
from fastapi import FastAPI, HTTPException

from app.database import Base, SessionLocal,engine
from app.model import plant
from app.model.plant import Plant

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

# @app.get("/plants",response_model=list[Plant],summary="Get All Plants",status_code=201)
# async def get_all_plants()->list[Plant]:
    
#     with open("../app/plant_db.json","r") as file:
#         plant = json.load(file)
#     result = plant
#     return result

# @app.get("/plant/{id}" , response_model=Plant , summary="Get Plant by Id")
# def get_plant_by_id(id:int)->Plant:
        
#     with open("../app/plant_db.json","r") as file:
#         plant = json.load(file)
        
#     for i in plant:
#         if i["id"] == id:
#             return Plant(**i)
    
#     raise HTTPException(status_code=404, detail={"error": "Plant not found"})