import os
from conn import Conn

GENDER = "female"
WEIGHT = "94"
HEIGHT = "160"
AGE = "35"
ENDPOINT = "https://trackapi.nutritionix.com/v2"

class Exercise:
    
    def __init__(self):
        try:
            NUTRI_API_KEY = os.environ['NUTRITIONIX_API_KEY']
        except:
            raise Exception("Environment variable NUTRITIONIX_API_KEY not found")
        try:
            NUTRI_API_ID = os.environ['NUTRITIONIX_API_ID']
        except:
            raise Exception("Environment variable NUTRITIONIX_API_ID not found")
        else:
            self.header = {
                "x-app-id": NUTRI_API_ID,
                "x-app-key": NUTRI_API_KEY,
                "Content-Type": "application/json"
            }


    def query_calories(self, query: str) -> dict:
        """ Connect in the api and get the calories information"""
        exercise_api = f"{ENDPOINT}/natural/exercise"
        query_json = {
            "query": query,
            "gender":"female",
            "weight_kg": WEIGHT,
            "height_cm": HEIGHT,
            "age": AGE
        }
        conn = Conn()
        data = conn.post_req(endpoint=exercise_api, query_json=query_json, header=self.header)
        return data
     
