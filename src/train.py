from sklearn.linear_model import LinearRegression
import pandas as pd
import pickle

DATA_PATH = "data/data.csv"

def train():
    data = pd.read_csv(DATA_PATH, header=None)
    y_name = data.columns[-1]
    X = data.drop(y_name,axis=1)
    y = data[y_name].values.reshape((-1,1))
    lr = LinearRegression()
    lr.fit(X,y)
    with open("model.pkl","wb") as file:
        pickle.dump(lr,file)