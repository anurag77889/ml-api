import numpy as np 
from app.core.model_loader import model 
from app.db.database import insert_prediction

def make_prediction(age: int, salary: float):
    features =np.array([[age, salary]])

    prediction = model.predict(features)[0]

    insert_prediction(age, salary, int(prediction))

    return int(prediction)
