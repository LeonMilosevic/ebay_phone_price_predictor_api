from flask import Flask, request
from decouple import config
from helpers import helper_functions
import pickle
import json
import psycopg2
import logging

# secrets
APP_MODEL_PATH = config("APP_MODEL_PATH")
APP_DATABASE = config("APP_DATABASE")
APP_USER = config("APP_USER")
APP_PASSWORD = config("APP_PASSWORD")
APP_HOST = config("APP_HOST")
APP_PORT = config("APP_PORT")

# load model from the file
pipe = pickle.load(open(APP_MODEL_PATH, "rb"))

db_connection = psycopg2.connect(
    database=APP_DATABASE,
    user=APP_USER,
    password=APP_PASSWORD,
    host=APP_HOST,
    port=APP_PORT,
)

app = Flask(__name__)


@app.route("/", methods=["GET"])
def display() -> str:
    if request.method == "GET":
        cursor = db_connection.cursor()
        try:
            results = helper_functions.get_results(cursor)
            cursor.close()
            return json.dumps({"success": results}), 200
        except:
            cursor.close()
            return json.dumps({"error": "something went wront"}), 500


@app.route("/predict", methods=["POST"])
def predict() -> str:
    if request.method == "POST":
        try:
            processed_input = helper_functions.process_input(request.data)
        except:
            return json.dumps({"error": "Please provide correct input"}), 500

        try:
            prediction = pipe.predict(processed_input)
        except:
            return json.dumps({"error": "something went wrong with the model"}), 500

        try:
            cursor = db_connection.cursor()
            post_data = json.loads(request.data)
            cursor.execute(
                f"""
                INSERT INTO predictions(brand, ram, storage, processor, camera, condition, evaluation) 
                VALUES('{post_data['brand']}',
                '{post_data['ram']}',
                '{post_data['storage']}',
                '{post_data['processor']}',
                '{post_data['camera']}',
                '{post_data['condition']}',
                '{float(prediction[0])}')
                """
            )

            db_connection.commit()
        except Exception as e:
            cursor.close()
            logging.warning(e)

        return json.dumps({"price": float(prediction[0])}), 200


if __name__ == "__main__":
    app.run()
