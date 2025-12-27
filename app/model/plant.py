import json
from typing import Optional
from fastapi import Body,FastAPI,HTTPException,Query
from pydantic import BaseModel,Field
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import Column, Integer, String
from app.database import Base

app = FastAPI(
    title="Plants API", 
    description="Plants FastAPI Example", 
    version="0.1.0"
)

class Plant(Base):
    __tablename__ = "plant"
    id = Column(
        Integer,
        primary_key=True,
        index=True,
        autoincrement=True
    )
    
    species : Mapped[str] = mapped_column(
        String(50), 
        unique=True
    )
    
    age = Column(
        Integer,
        index=True
    )
    
    habitat = Column(
        Integer,
        index=True
    )

# class UpdatePlant(BaseModel):
#     name: Optional[str] = Field(None, description="Plant name")
#     species: Optional[str] = Field(None, description="Plant species")
#     age: Optional[int] = Field(None, description="Plant age")
#     habitat: Optional[str] = Field(None, description="Plant habitat")
#     diet: Optional[str] = Field(None, description="Plant diet")