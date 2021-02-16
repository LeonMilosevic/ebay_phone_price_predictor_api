# PHONE PRICE PREDICTOR FLASK API - Turing College Capstone-Project

FLASK API to help you evaluate your phones price before putting it for sale on E-bay 

### Introduction

API that will help you evaluate the price of your phone based on given features.

### Technologies used
- Python
- JSON
- Numpy
- decouple
- Pickle
- SKlearn
- DecissionTreeRegressor

### How to use it?

Send a json POST request to https://phone-evaluator.herokuapp.com/predict

{\
    "ram": 4.0,\
    "storage": 256.0,\
    "processor": 3.0,\
    "camera": 12.0,\
    "brand": "apple",\
    "condition": "used"\
}

returns:

{"evaluation": 1112.726956521739}