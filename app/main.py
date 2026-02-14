from fastapi import FastAPI
from pydantic import BaseModel
import pickle
import numpy as np 

app = FastAPI()

# Data contract
class PredictionInput(BaseModel):
    age: int
    salary: float

@app.get("/health")
def health_check():
    return {"Status": "API is running"}

@app.post("/predict")
def predict(input_data: PredictionInput):
    return {
        "received_age": input_data.age,
        "received_salary": input_data.salary
    }
