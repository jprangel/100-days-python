import os
from conn import Conn
from datetime import datetime

ENDPOINT = "https://api.sheety.co/086db200995912863fe4fd34860400b8/jessicaWorkouts/workouts"

class Sheet:
    
    def __init__(self):
        try:
            SHEETY_TOKEN = os.environ['SHEETY_TOKEN']
        except:
            raise Exception("Enviroment variable SHEETY_TOKEN not found")
        else:
            self.header = {
                "Authorization": f"Bearer {SHEETY_TOKEN}"
            }
    
    def get_date_time(self):
        """ Get the current date and format it"""
        date = datetime.now().date()
        date = date.strftime('%d/%m/%Y')
        time = datetime.now().time()
        time = time.strftime('%H:%M:%S')
        return (date,time)
    
    def update_row(self, info):
        """ Post the exercises information in the google spreedsheet"""
        date_time = self.get_date_time()
        for i in info['exercises']:
            query = {
                "workout": {
                    "date":	date_time[0],
                    "time": date_time[1],
                    "exercise": i['name'].title(),
                    "duration": int(i['duration_min']),
                    "calories": int(i['nf_calories'])
                    }
                }
            conn = Conn()
            try:
                conn.post_req(query_json=query, endpoint=ENDPOINT, header=self.header)
            except:
                raise Exception("Update in the spreadsheet has an error")
            else:
                print("Information updated into spreadsheet sucessfully")