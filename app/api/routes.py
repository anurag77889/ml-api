from fastapi import APIRouter, HTTPException, Depends
from pydantic import BaseModel
from app.services.prediction_service import make_prediction

router = APIRouter()

# Data contract
class PredictionInput(BaseModel):
    age: int
    salary: float

def get_prediction_service():
    return make_prediction

@router.post("/predict")
def predict(
    input_data: PredictionInput, prediction_service=Depends(get_prediction_service)
    ):

    try:
        result = prediction_service(input_data.age, input_data.salary)
        return {"prediction": result}
    
    except Exception:
        raise HTTPException(
            status_code=500,
            detail="Prediction failed. Please try again later."
        )
    