from typing import Optional
from pydantic import BaseModel


class PlantResponse(BaseModel):
    id:int
    species: str
    age: int
    habitat: int