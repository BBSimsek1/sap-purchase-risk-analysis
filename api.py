from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def home():
    return {
    "message": "SAP Purchase Risk Analysis API is running."
    }