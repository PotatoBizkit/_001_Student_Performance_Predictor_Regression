from flask import Flask, request, jsonify
import joblib
import numpy as np

model = joblib.load("_001_Student_Performance_Simple_Linear_Regression.pkl")

app = Flask(__name__)

@app.route("/")
def home():
    return "Flask ML Model is Running!"

@app.route("/predict", methods=["POST"])
def predict():
    try:
        
        data = request.json
        features = np.array(data["features"]).reshape(1, -1)

        prediction = model.predict(features)[0]

        return jsonify({"prediction": prediction})

    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == "__main__":
    app.run(debug=True)
