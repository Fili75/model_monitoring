import pickle

def predict(x):
    with open("model.pkl", "rb") as file:
        model = pickle.load(file)
    return model.predict(x)