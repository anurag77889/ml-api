from fastapi import FastAPI

app = FastAPI()

@app.get("/health")
def health_check():
    return {"Status": "API is running"}

