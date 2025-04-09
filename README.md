# Model monitoring

An example of model monitoring with FastAPI, Grafana and Prometheus

## Set up
- Open a terminal and run docker compose up to set up Grafana and Prometheus. Grafana will be available at http://127.0.0.1:3000, while
Prometheus address will be http://127.0.0.1:9090
- Run uvicorn app:app --port 3100 on a terminal 
- Log in Grafana. The default username/password are admin/admin. It requires a change password step after the first login
- Go to Connections > Data sources and click on Add new data source. Choose Prometheus.
 In Connection > Prometheus server URL write http://prometheus:9090, then save.
- In Dashboards click on Create Dashboard and then Add visualization. Select prometheus as data source. In the new page
select Data_mean_difference in Metric.

## How to use the service
- curl -X GET http://127.0.0.1/model_train to train the model. It is a three-parameters linear model trained on the toy dataset data/data.csv
- curl -X POST http://127.0.0.1:3100/model_predict -H "Content-Type: application/json" -d {\"x\":X_VALUE,\"y\":Y_VALUE,\"z\":Z_VALUE} to make predictions