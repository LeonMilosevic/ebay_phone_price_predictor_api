import numpy as np
import json
import pandas as pd

def clean_input(input: str) -> list:
    ram = json.loads(input)['ram']
    storage = json.loads(input)['storage']
    processor = json.loads(input)['processor']
    camera = json.loads(input)['camera']
    brand_apple: int
    brand_huawei: int
    brand_samsung: int
    condition_new: int
    condition_used: int
    if json.loads(input)['brand'].lower() == 'apple':
        brand_apple = 1
        brand_huawei = 0
        brand_samsung = 0
    elif json.loads(input)['brand'].lower() == 'huawei':
        brand_apple = 0
        brand_huawei = 1
        brand_samsung = 0
    else:
        brand_apple = 0
        brand_huawei = 0
        brand_samsung = 1
    
    if json.loads(input)['condition'].lower() == "new":
        condition_new = 1
        condition_used = 0
    else:
        condition_new = 0
        condition_used = 1

    return [ram, storage, processor, camera, brand_apple, brand_huawei, brand_samsung, condition_new, condition_used]

def process_input(input: str) -> np.array:
    cleaned_input = clean_input(input)

    return np.asarray([cleaned_input])
