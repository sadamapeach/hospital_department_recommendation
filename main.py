from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from llm_utils import get_recommended_department

app = FastAPI()

class PatientInfo(BaseModel):
    gender: str
    age: int
    symptoms: list[str]

@app.post("/recommend")
def recommend_department(info: PatientInfo):
    try:
        department = get_recommended_department(info.gender, info.age, info.symptoms)
        return {"recommended_department": department}
    except Exception as e:
        print(f"ERROR INTERNAL: {e}")
        raise HTTPException(status_code=500, detail=str(e))