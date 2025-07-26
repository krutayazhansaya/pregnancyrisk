from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
import joblib
import pandas as pd

app = FastAPI()

# Define the input data model using Pydantic
class HealthInput(BaseModel):
    age: int = Field(..., alias="Age")
    systolic_bp: int = Field(..., alias="Systolic BP")
    diastolic: int = Field(..., alias="Diastolic")
    bs: int = Field(..., alias="BS")
    body_temp: int = Field(..., alias="Body Temp")
    bmi: int = Field(..., alias="BMI")
    previous_complications: int = Field(..., alias="Previous Complications")
    preexisting_diabetes: int = Field(..., alias="Preexisting Diabetes")
    gestational_diabetes: int = Field(..., alias="Gestational Diabetes")
    mental_health: int = Field(..., alias="Mental Health")
    heart_rate: int = Field(..., alias="Heart Rate")

# Load the trained pipeline using joblib
model_path = "./models/catboost_model.joblib"
pipeline = joblib.load(model_path)

@app.post("/predict")
async def predict_risk(data: HealthInput):
    try:
        # Convert input data to DataFrame using aliases (important!)
        input_data = pd.DataFrame([data.dict(by_alias=True)])

        # Make prediction using the pipeline
        prediction = pipeline.predict(input_data)
        probability = pipeline.predict_proba(input_data)[0].tolist()

        return {
            "prediction": int(prediction[0]),
            "probability": probability[1],
            "status": "success"
        }

    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.get("/")
async def root():
    return {"message": "Pregnancy Risk Prediction API. Use POST /predict."}

# from fastapi import FastAPI

# app = FastAPI()

# @app.get("/")
# def root():
#     return {"message": "Hello World"}
