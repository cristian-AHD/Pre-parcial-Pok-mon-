from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class pokemon(BaseModel):
    id:int
    nombre:str
    life:int
    attack:int
    type:str
    leavepokeball:bool=True