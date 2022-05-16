import requests
import pickle
from google.cloud import storage
import numpy as np

storage_client = storage.Client()
bucket = storage_client.get_bucket('model-bucket-iris')
blob = bucket.blob('flower-v1.pkl')
blob.download_to_filename('/tmp/flower-v1.pkl')
model_pk = pickle.load(open('/tmp/flower-v1.pkl', 'rb'))

def api_predict(request):
    if request.method == 'GET':
        return "Please Send POST Request"
    elif request.method == 'POST':
        
        data = request.get_json()
        
        sepal_length = data["sepal_length"]
        sepal_width = data["sepal_width"]
        petal_length = data["petal_length"]
        petal_width = data["petal_width"]
    
        data = np.array([[sepal_length, sepal_width, 
                          petal_length, petal_width]])
           
        prediction = model_pk.predict(data)
        return str(prediction)
