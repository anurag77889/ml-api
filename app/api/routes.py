from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from app.services.prediction_service import make_prediction

router = APIRouter()

# Data contract
class PredictionInput(BaseModel):
    age: int
    salary: float

@router.post("/predict")
def predict(input_data: PredictionInput):

    try:
        result = make_prediction(input_data.age, input_data.salary)
        return {"prediction": result}
    
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail="Prediction failed. Please try again later."
        )
    