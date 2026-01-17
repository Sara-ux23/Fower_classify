from flask import Flask, request, jsonify, render_template # Add render_template
from flask_cors import CORS
import joblib

app = Flask(__name__)
CORS(app)

model = joblib.load("iris_knn_model.pkl")
iris_species = ['setosa', 'versicolor', 'virginica']

@app.route('/')
def home():
    # Change this line to render the HTML file
    return render_template('index.html') 

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    sample = [[
        data['sepal_length'],
        data['sepal_width'],
        data['petal_length'],
        data['petal_width']
    ]]
    predicted_class = model.predict(sample)[0]
    return jsonify({'species': iris_species[predicted_class]})

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)