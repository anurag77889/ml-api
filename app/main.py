from fastapi import FastAPI
from pydantic import BaseModel
import pickle
import numpy as np 

app = FastAPI()

# Load model once when app starts
with open("E:\\AI-ML Engineer\\ml-api\\model\\model.pkl", "rb") as f:
    model = pickle.load(f)

# Data contract
class PredictionInput(BaseModel):
    age: int
    salary: float

@app.get("/health")
def health_check():
    return {"Status": "API is running"}

@app.post("/predict")
def predict(input_data: PredictionInput):

    # Convert input to model formate
    features = np.array([[input_data.age, input_data.salary]])

    prediction = model.predict(features)[0]

    return {
        "prediction": int(prediction)
    }
