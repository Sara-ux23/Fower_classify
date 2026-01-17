import requests
    "sepal_length": 5.1,
    "petal_width": 0.2
}

# Sending the request
response = requests.post("http://127.0.0.1:5000/predict", json=data)

# Printing what the server says back
print(response.json())