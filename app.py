import pandas as pd
from fastapi import FastAPI
from endpoints import (
    model_train,
    model_predict
)
from prometheus_fastapi_instrumentator import Instrumentator
from typing import Callable
from prometheus_fastapi_instrumentator.metrics import Info
import prometheus_client
import os

def read_data():
    d = pd.DataFrame({})
    for year in os.listdir("data_endpoint/predict"):
        for month in os.listdir(f"data_endpoint/predict/{year}"):
            for day in os.listdir(f"data_endpoint/predict/{year}/{month}"):
                for file in os.listdir(f"data_endpoint/predict/{year}/{month}/{day}"):
                    new_data = pd.read_csv(f"data_endpoint/predict/{year}/{month}/{day}/{file}",header=None, index_col=None)
                    d = pd.concat([d, new_data])
    return d


def data_info() -> Callable[[Info], None]:
    METRIC_MEAN_DIFFERENCE = prometheus_client.metrics.Gauge("Data_mean_difference","Info about data mean difference")

    def instrumentation(info: Info) -> None:
        data_endpoint = read_data()
        if data_endpoint.empty:
            predict_mean = 0
        else:
            predict_mean = data_endpoint.mean(axis=0).to_dict()[0]
        data_info= pd.read_csv("data/data.csv").mean(axis=0)[0] - predict_mean
        METRIC_MEAN_DIFFERENCE.set(data_info)
    return instrumentation

app = FastAPI(debug=True)
Instrumentator().instrument(app).expose(app)
Instrumentator().instrument(app).add(data_info())
app.include_router(model_train.router)
app.include_router(model_predict.router)
