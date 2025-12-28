from typing import Optional
from pydantic import BaseModel


class PlantRequest(BaseModel):
    species: str
    age: int
    habitat: int