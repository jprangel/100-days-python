from conn import Conn
import os

ENDPOINT = "https://api.tequila.kiwi.com"
ADULTS = 1
CABIN = "M" #Economic
CURRENCY = "EUR"
SORT_BY = "duration"

class FlightSearch:
    #This class is responsible for talking to the Flight Search API.
    def __init__(self) -> None:
        self.conn = Conn()
        try:
            token = os.environ['KIWI_APITOKEN']
        except:
            raise Exception("Environment variable KIWI_APITOKEN not found")
        self.header = { 
            "apikey": f"{token}"
        }
        self.currency = CURRENCY
        self.search_api = f"{ENDPOINT}/v2/search"
    
    def search_flight(self, f_from: str, f_to: str, f_date_from: str, f_date_to: str, nights_in_dst_to: int, stopsover: int):
        self.payload = {
            "fly_from": f_from ,
            "fly_to": f_to ,
            "dateFrom": f_date_from,
            "dateTo": f_date_to,
            "adults": ADULTS,
            "selected_cabins": CABIN,
            "curr": self.currency,
            "sort": SORT_BY,
            "flight_type": "round",
            "nights_in_dst_from": 2,
            "nights_in_dst_to": nights_in_dst_to,
            "max_stopovers": stopsover
        }
        data = self.conn.get_req(endpoint=self.search_api, header=self.header, param=self.payload)
        return data