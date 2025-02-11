from fastapi import FastAPI
from processor import filterData

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Fast FlyBy API"}

@app.get("/api/aircraft")
def get_aircraft():
    try:
        return filterData()
    except Exception as e:
        return {"error": str(e)}