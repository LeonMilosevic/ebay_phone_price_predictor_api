# PHONE PRICE PREDICTOR FLASK API - Turing College Capstone-Project

FLASK API to help you evaluate your phones price before putting it for sale on E-bay 

### Introduction

API that will help you evaluate the price of your phone based on given features.

### How to use it?

Install prerequisites from requirements.txt

Send a json POST request to https://phone-evaluator.herokuapp.com/predict

```JSON
{
    "ram": 4.0,
    "storage": 256.0,
    "processor": 3.0,
    "camera": 12.0,
    "brand": "apple",
    "condition": "used"
}
```
returns:

```JSON
{"price": 1112.726956521739}
```