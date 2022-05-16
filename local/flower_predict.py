# -*- coding: utf-8 -*-

from flask import Flask, request
import pickle
import numpy as np

app = Flask(__name__)

# http://localhost:5000/api_predict
model_pk = pickle.load(open("flower-v1.pkl", "rb"))

@app.route('/api_predict', methods=["GET", "POST"])
def api_predict():
    if request.method == "GET":
        return "Please send Post Request"
    elif request.method == "POST":
        data = request.get_json()
        
        sepal_length = data['sepal_length'] 
        sepal_width = data["sepal_width"]
        petal_length = data["petal_length"]
        petal_width = data["petal_width"]
        
        in1 = np.array([[sepal_length, sepal_width , petal_length, petal_width]])
        
        prediction = model_pk.predict(in1)
        
        return str(prediction)
    
app.run()


import requests

url = "http://localhost:5000/api_predict"
data = {
        "sepal_length" : 10,
        "sepal_width":0.1,
         "petal_length":0,
         "petal_width":10
        
        }

r = requests.post(url, json = data)
print(r)
print(r.text)





















































import requests
url = "http://localhost:5000/api_predict"
data = {
         "sepal_length" : 0.1,
         "sepal_width":0.1,
         "petal_length":0,
         "petal_width":10
        }

r = requests.post(url, json = data)
print(r)
print(r.text)


