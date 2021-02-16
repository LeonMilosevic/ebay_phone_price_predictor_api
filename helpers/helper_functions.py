import numpy as np
import json

def process_input(input: str) -> list:
    """[extracts the json from the input,
        prepares the data as it is needed for the model to accept it,
        returns a np.array of float numbers to be evaluated by the model]

    Args:
        input (str): [JSON object from the post request]

    Returns:
        list: [of int that have been transformed from json object]
    """

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

    return np.asarray([ram, storage, processor, camera, brand_apple, brand_huawei, brand_samsung, condition_new, condition_used])

def get_results(cursor):

    cursor.execute(

        '''
        SELECT * 
        FROM predictions
        ORDER BY created_at DESC
        LIMIT 10
        ''')

    rows = cursor.fetchall()
    
    results = [
        {
            "id": row[0],
            "brand": row[1], 
            "ram": float(row[2]), 
            "storage": float(row[3]), 
            "processor": float(row[4]), 
            "camera":float(row[5]), 
            "condition":row[6], 
            "evaluation": float(row[7]), 
            "dateCreated": str(row[8])
        } 
        for row in rows]
        
    return results