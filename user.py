import pickle
import numpy as np
import pandas as pd

test = pd.read_excel("sheets/test.xlsx")

def getDataFromModel(row):
    model = pickle.load(open("models/model.pkl", "rb"))

    print("Hello")
    data = row

    data = np.array(data.split(","))
    data = data.reshape(1, -1)

    return f"This row belongs to cluster {model.predict(data)[0]}"

def getDataFromSVMModel():
    model = pickle.load(open("models/svmModel.pkl", "rb"))
    return model.predict(test)

def getDataFromTreeModel():
    model = pickle.load(open("models/treeModel.pkl", "rb"))
    return model.predict(test)

def getDataFromKNNModel():
    model = pickle.load(open("models/KNNModel.pkl", "rb"))
    return model.predict(test)
