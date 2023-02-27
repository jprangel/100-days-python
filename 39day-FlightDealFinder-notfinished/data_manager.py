import os
from conn import Conn

ENDPOINT = "https://api.sheety.co/086db200995912863fe4fd34860400b8/jessicaFlightDeals/prices"

class DataManager:
    
    def __init__(self) -> None:
        self.conn = Conn()
        try:
            token = os.environ['SHEETY_TOKEN_FLIGHT']
        except:
            raise Exception("Environment variable SHEETY_TOKEN_FLIGHT not found")
        else:  
            self.header = {
                "Authorization": f"Bearer {token}"
            }
        
    def get_info(self):
        info = self.conn.get_req(endpoint=ENDPOINT, header=self.header, param="")
        return info