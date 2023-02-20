import requests
import os
from datetime import datetime, timedelta, timezone

URL = "https://www.alphavantage.co/query"

class Stock:
    
    def __init__(self, stock):
        self.stock = stock
        try:
            API_KEY = os.environ.get('STOCK_API_KEY')
        except:
            raise Exception("Environment variable STOCK_ACESS_KEY doesn't exist")
        else:
            self.param = { "function" : "TIME_SERIES_DAILY_ADJUSTED",
                    "symbol": self.stock,
                    "interval": "30min",
                    "apikey": API_KEY 
                }
            
    def fetch_data(self):
        r = requests.get(URL, params=self.param)
        r.raise_for_status()
        self.data = r.json()
        
    def get_dates(self):
        self.yesterday = datetime.now(timezone.utc).date() + timedelta(days=-1)
        self.before_yesterday = datetime.now(timezone.utc).date() + timedelta(days=-2)
        
    def parse_stock_trade(self):
        try:
            self.fetch_data()
        except:
            raise Exception("Get stock trade error")
        try:
            self.get_dates()
        except: 
            raise Exception("Get dates error")
        else:
            self.stock_close_yesterday = self.data['Time Series (Daily)'][str(self.yesterday)]['4. close']
            self.stock_close_before_yesterday = self.data['Time Series (Daily)'][str(self.before_yesterday)]['4. close']
    
    def get_percentage(self, stock_y: float, stock_by: float):
        return ((stock_y - stock_by) / stock_by) * 100
        