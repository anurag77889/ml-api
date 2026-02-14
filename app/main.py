from fastapi import FastAPI
from app.api.routes import router
from app.db.database import create_table

app = FastAPI()

create_table()

app.include_router(router)

@app.get("/health")
def health_check():
    return {"Status": "API is running"}

