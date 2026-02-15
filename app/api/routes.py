from fastapi import APIRouter, HTTPException, Depends
from pydantic import BaseModel
from app.services.prediction_service import make_prediction
from app.db.database import get_recent_predictions

router = APIRouter()

# Data contract
class PredictionInput(BaseModel):
    age: int
    salary: float

def get_prediction_service():
    return make_prediction

# PREDICT router for predictions
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
    
# HISTORY router for history
@router.get("/history")
def get_history(limit: int = 10):
    
    try:
        data = get_recent_predictions(limit)

        return {
            "history": [
                {
                    "age": row[0],
                    "salary": row[1],
                    "prediction": row[2],
                    "created_at": row[3]
                }
                for row in data
            ]
        }
    except Exception:
        raise HTTPException(
            status_code=500,
            detail="Failed to fetch history"
        )