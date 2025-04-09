import json

import pandas as pd
from fastapi import APIRouter
from fastapi.responses import  JSONResponse
from pydantic import BaseModel
from src.predict import predict
import numpy as np
import os
import time
router = APIRouter()

class PredictItem(BaseModel):
    x: float
    y: float
    z: float


@router.post("/model_predict")
def model_predict(item: PredictItem):
    input = np.array([item.x,item.y,item.z])
    ###input register
    date = time.localtime()
    year = date.tm_year
    month = date.tm_mon
    day = date.tm_mday
    root = "data_endpoint/predict"
    path = f"{root}/{year}/{month}/{day}"
    try:
        os.mkdir(f"{root}/{year}")
    except:
        pass
    try:
        os.mkdir(f"{root}/{year}/{month}")
    except:
        pass
    try:
        os.mkdir(path)
    except:
        pass
    file_name = f"{date.tm_hour}{date.tm_min}.csv"


#    input.tofile(path+f"/{date.tm_hour}{date.tm_min}{date.tm_sec}.json")
    input =input.reshape((1,-1))
    if file_name in os.listdir(path):
        data = pd.read_csv(path+"/" +file_name,header=None, index_col=None)
        pd.concat([data,pd.DataFrame(input)]).to_csv(path+"/" +file_name, header=None, index=False)
    else:
        pd.DataFrame(input).to_csv(path+"/" +file_name, header=None, index=False)
    return JSONResponse({"response": predict(input).tolist()})