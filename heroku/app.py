# -*- coding: utf-8 -*-
"""
Created on Wed Feb 12 21:24:17 2020

@author: PC
"""

from flask import Flask, request
import pickle
import numpy as np
from sklearn.linear_model import LogisticRegression

app = Flask(__name__)

# http://localhost:5000/api_predict

model_pk = pickle.load(open("flower-v1.pkl","rb"))


@app.route('/api_predict', methods = ['POST','GET'])
def api_predict():
    if request.method == 'GET':
        return "Please Send POST Request"
    elif request.method == 'POST':
        
        print("Hello" + str(request.get_json()))
        
        data = request.get_json()
        
        sepal_length = data["sepal_length"]
        sepal_width = data["sepal_width"]
        petal_length = data["petal_length"]
        petal_width = data["petal_width"]
    
        data = np.array([[sepal_length, sepal_width, 
                          petal_length, petal_width]])
           
        prediction = model_pk.predict(data)
        return str(prediction)

if __name__ == "__main__":
    app.run()