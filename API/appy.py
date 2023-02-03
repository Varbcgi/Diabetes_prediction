# -*- coding: utf-8 -*-


import asyncio
from fastapi import FastAPI,Body
from pydantic import BaseModel
import uvicorn
import pickle
import numpy as np

app = FastAPI()

# load your ML model
model = pickle.load(open("model.pkl", "rb"))


class Features(BaseModel):
    
    feature_list=[]    
    HighBP: float                
    HighChol: float               
    CholCheck: float              
    BMI: float                    
    Smoker: float                 
    Stroke: float                 
    HeartDiseaseorAttack: float   
    PhysActivity: float           
    Fruits: float                 
    Veggies: float                
    HvyAlcoholConsump: float      
    AnyHealthcare: float          
    NoDocbcCost: float            
    GenHlth: float                
    MentHlth: float               
    PhysHlth: float               
    DiffWalk: float               
    Sex: float                    
    Age: float                    
    Education: float              
    Income: float 



@app.post("/predict")
async def predict(features: Features = Body()):
    # convert the input data into the format required by your model
    
    features_list = [
        features.HighBP,
        features.HighChol,
        features.CholCheck,
        features.BMI,
        features.Smoker,
        features.Stroke,
        features.HeartDiseaseorAttack,
        features.PhysActivity,
        features.Fruits,
        features.Veggies,
        features.HvyAlcoholConsump,
        features.AnyHealthcare,
        features.NoDocbcCost,
        features.GenHlth,
        features.MentHlth,
        features.PhysHlth,
        features.DiffWalk,
        features.Sex,
        features.Age,
        features.Education,
        features.Income
    ]
    features = (np.array(features_list)).reshape(1, -1)
    # use the model to make predictions
    prediction = model.predict(features)
    
    # return the prediction results
    return {"prediction": prediction.tolist()}
    

