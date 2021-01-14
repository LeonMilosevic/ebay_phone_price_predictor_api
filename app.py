import pickle
import json
from flask import Flask, request
from decouple import config
from helpers import helper_func
from db import db
import psycopg2

# secrets
APP_MODEL_PATH = config("APP_MODEL_PATH")
APP_DATABASE = config('APP_DATABASE')
APP_USER = config('APP_USER')
APP_PASSWORD = config('APP_PASSWORD')
APP_HOST = config('APP_HOST')
APP_PORT = config('APP_PORT')

# load model from the file
regressor = pickle.load(open(APP_MODEL_PATH, "rb"))

db_connection = db.database_connect(
    database=APP_DATABASE,
    user=APP_USER, 
    password=APP_PASSWORD, 
    host=APP_HOST, 
    port=APP_PORT)

app = Flask(__name__)

@app.route("/", methods=["GET"])
def display() -> str:
    if request.method == "GET":
        cursor = db_connection.cursor()
        try:
            cursor.execute('SELECT * FROM predictions')
            rows = cursor.fetchall()
            print(rows)
            results = [{"id": row[0], "brand": row[1], "ram": float(row[2]), "storage": float(row[3]), "processor": float(row[4]), "camera":float(row[5]), "condition":row[6], "evaluation": float(row[7])} for row in rows]
            cursor.close()
            return json.dumps({"success": results}), 200
        except EnvironmentError as error:
            cursor.close()
            print(error)
            return json.dumps({"error": "something went wront"}), 500

@app.route("/predict", methods=["POST"])
def predict() -> str:
    if request.method == "POST":
        processed_input = helper_func.process_input(request.data)

        try:
            prediction = regressor.predict(processed_input)
        except:
            return json.dumps({"error": "something went wrong, please try again"}), 500
        
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
                """)    

            db_connection.commit()
        except:
            cursor.close()
            return json.dumps({"error": "please try again later"}), 500
        
        return json.dumps({"evaluation": float(prediction[0])}), 200

if __name__ == "__main__":
    app.run(debug=True)