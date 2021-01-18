# -*- coding: utf-8 -*-
"""
Created on Mon Jan 18 15:22:18 2021

@author: a.e.kumar.jaiswal
"""

from pydantic import BaseModel


### create class using pydantic Base model for prediction
class Customer_datas(BaseModel):
    CreditScore: int
    Age : int
    Tenure : int
    Balance: int
    NumOfProducts: int
    HasCrCard: int
    IsActiveMember: int
    EstimatedSalary: int
    Male  : int
    Germany: int
    Spain: int
    
from fastapi import FastAPI
import uvicorn
import pickle
import pandas as pd

## Create app object for fastapi
app = FastAPI()

## load the model.pkl
churn=pickle.load(open('model.pkl','rb'))

## index route, opens on port mentioned using 5000

@app.get("/")
def index():
    return {"Hello": "World"}




@app.post('/predict')
def predict_customer_churn(data:Customer_datas):
    data=data.dict()
    CreditScore= data['CreditScore']
    Age = data['Age']
    Tenure = data['Tenure']
    Balance= data['Balance']
    NumOfProducts= data['NumOfProducts']
    HasCrCard= data['HasCrCard']
    IsActiveMember= data['IsActiveMember']
    EstimatedSalary= data['EstimatedSalary']
    Male  = data['Male']
    Germany= data['Germany']
    Spain= data['Spain']
    prediction=churn.predict([[CreditScore,Age,Tenure,Balance,NumOfProducts,HasCrCard,
IsActiveMember,EstimatedSalary,  Male,  Germany , Spain]])
    print(prediction)
    if(prediction[0]>0.5):
        prediction="customer churn"
    else:
        prediction="customer will not churn"
    return {'prediction':prediction}

    



# if __name__=='__main__':
#     uvicorn.run(app,host='127.0.0.1',port=5000)


# uvicorn main:app --reload --port 5000
    
