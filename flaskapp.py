
flaskapp.py

Page
1
/
1
100%
import pickle
import pandas as pd
import numpy as np
from flask import Flask, request, render_template

app = Flask(__name__)

# Load the trained model
model = pickle.load(open("model.pkl", "rb"))

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    # Get form data
    hrs_studied = float(request.form["hrs_studied"])
    prev_score = float(request.form["prev_score"])
    sleep = float(request.form["sleep"])
    sample_practiced = int(request.form["sample_practiced"])
    extra_curr = 1 if request.form["extra_curr"].lower() == "yes" else 0

    # Prepare features for prediction
    feature_names = ["hrs_Studied", "prev_score", "sleep", "sample_practiced", "extra_Curr"]
    features = pd.DataFrame([[hrs_studied, prev_score, sleep, sample_practiced, extra_curr]], columns=feature_names)

    # Predict result
    prediction = model.predict(features)
    formatted_prediction = f"The predicted result is {round(float(prediction[0]), 2)}"

    return render_template("result.html", prediction=formatted_prediction)


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
Displaying flaskapp.py.
