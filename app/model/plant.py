import json
from typing import Optional
from fastapi import Body,FastAPI,HTTPException,Query
from pydantic import BaseModel,Field

app = FastAPI(
    title="Plants API", description="Plants FastAPI Example", version="0.1.0"
)

class Plant(BaseModel):
    name:str = Field(
        min_length=2,description="Plant Name"
    )
    species:str=Field(
        min_length=2,description="Plant Species"
    )
    age:int = Field(
        min_length=2,description="Plant Age"
    )
    habitat:str=Field(
        min_length=2,description="Habitat Plant"
    )


class UpdatePlant(BaseModel):
    name: Optional[str] = Field(None, description="Plant name")
    species: Optional[str] = Field(None, description="Plant species")
    age: Optional[int] = Field(None, description="Plant age")
    habitat: Optional[str] = Field(None, description="Plant habitat")
    diet: Optional[str] = Field(None, description="Plant diet")

