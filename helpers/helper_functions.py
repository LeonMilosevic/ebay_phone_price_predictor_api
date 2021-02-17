import json
import pandas as pd

def process_input(input: str) -> pd.DataFrame:
    """[extracts the json from the input,
        prepares the data as it is needed for the model to accept it,
        returns a dataframe to be preprocessed by our pipeline]

    Args:
        input (str): [JSON object from the post request]

    Returns:
        pd.DataFrame: [dataframe to be processed by pipeline]
    """
    x = {
        'brand': [json.loads(input)['brand']],
        'ram': [json.loads(input)['ram']],
        'processor': [json.loads(input)['processor']], 
        'condition': [json.loads(input)['condition']],
        'storage': [json.loads(input)['storage']], 
        'camera': [json.loads(input)['camera']], 
        'model': [json.loads(input)['model']]
        }
    df = pd.DataFrame(data=x)

    return df

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