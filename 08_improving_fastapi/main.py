from fastapi import FastAPI
from fastapi.responses import JSONResponse
import sys
import os 
from schema import UserInput,PredictionResponse
from model.predict import predict_output,MODEL_VERSION



sys.path.append(os.path.dirname(os.path.abspath(__file__)))


app=FastAPI()
    

@app.get("/")
def home():
    return {"message":"Insurance Premium Prediction API."}
        

@app.get("/health")
def health_check():
    return {"Status":"OK",
            "version":MODEL_VERSION}
        

@app.post("/predict",response_model=PredictionResponse)
def predict_premium(data:UserInput):
    try:
        user_input={
            'bmi':data.bmi,
            'age_group':data.age_group,
            'lifestyle_risk':data.lifestyle_risk,
            'city_tier':data.city_tier,
            'income_lpa':data.income_lpa,
            'occupation':data.occupation   

        }
        result=predict_output(user_input)

        return JSONResponse(status_code=200,content={'response':result})
    except Exception as e:
        return JSONResponse(status_code=500,content={"message":str(e)})

