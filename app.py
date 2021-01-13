import pickle
import json
from flask import Flask, request
from decouple import config
from helpers import helper_func

# secrets
APP_MODEL_PATH = config("APP_MODEL_PATH")

# load model from the file
regressor = pickle.load(open(APP_MODEL_PATH, "rb"))


app = Flask(__name__)

@app.route("/predict", methods=["POST"])
def predict() -> str:
    processed_input = helper_func.process_input(request.data)
    
    try:
        prediction = regressor.predict(processed_input)
    except:
        return json.dumps({"error": "something went wrong, please try again"}), 500
    return json.dumps({"Prediction": float(prediction[0])}), 200

if __name__ == "__main__":
    app.run(debug=True)