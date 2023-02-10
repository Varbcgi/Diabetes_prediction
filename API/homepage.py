# -*- coding: utf-8 -*-


from flask import Flask, request, render_template
import requests

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/predict", methods=["POST"])
def predict():
    data = {
        "HighBP": request.form["HighBP"],
        "HighChol": request.form["HighChol"],
        "CholCheck": request.form["CholCheck"],
        "BMI": request.form["BMI"],
        "Smoker": request.form["Smoker"],
        "Stroke": request.form["Stroke"],
        "HeartDiseaseorAttack": request.form["HeartDiseaseorAttack"],
        "PhysActivity": request.form["PhysActivity"],
        "Fruits": request.form["Fruits"],
        "Veggies": request.form["Veggies"],
        "HvyAlcoholConsump": request.form["HvyAlcoholConsump"],
        "AnyHealthcare": request.form["AnyHealthcare"],
        "NoDocbcCost": request.form["NoDocbcCost"],
        "GenHlth": request.form["GenHlth"],
        "MentHlth": request.form["MentHlth"],
        "PhysHlth": request.form["PhysHlth"],
        "DiffWalk": request.form["DiffWalk"],
        "Sex": request.form["Sex"],
        "Age": request.form["Age"],
        "Education": request.form["Education"],
        "Income": request.form["Income"]

    }

    response = requests.post("http://localhost:8000/predict", json=data)
    print("Here")
    if response.status_code == 200:
        prediction = response.json()["prediction"]
        return render_template("predict.html", prediction=prediction)
    else:
        return "Failed to get prediction."


if __name__ == "__main__":
    app.run(debug=True)
