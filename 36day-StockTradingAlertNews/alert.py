import requests
import os
from twilio.rest import Client
from twilio.http.http_client import TwilioHttpClient

FROM_TWILLO = "+19257225867"
TWILLO_ACC_ID = "AC8b9c413eaebd8bd6a525db3b07b9a3bd"
# The configuration below is necessary to run in python anywhere website with a free account
#proxy_client = TwilioHttpClient()
#proxy_client.session.proxies = {'https': os.environ['https_proxy']}

class Alert:
    
    def __init__(self) -> None:
        try:
            self.TWILIO_AUTH_TOKEN = os.environ.get('TWILIO_AUTH_TOKEN')
        except:
            raise Exception("Environment variable TWILIO_AUTH_TOKEN doesn't exist")
        try:
            self.TO_MYNUM = os.environ.get('MY_PHONENUM')
        except:
            raise Exception("Environment variable MY_PHONENUM doesn't exist")
        
    def send_news_sms(self, msg: tuple, stock: str, percent: float):
        # The configuration below is necessary to run in python anywhere website with a free account
        #client = Client(TWILLO_ACC_ID, self.TWILIO_AUTH_TOKEN, http_client=proxy_client)
        client = Client(TWILLO_ACC_ID, self.TWILIO_AUTH_TOKEN)
        if percent > 0:
            stock_msg = f"{stock}: 🔺{int(percent)}%"
        else:
            stock_msg = f"{stock}: 🔻{abs(int(percent))}%"
        for i in msg:
            msg_to_sms = f"{stock_msg}\n Source: {i[0]}\nHeadline: {i[1]}\nBrief: {i[2]}\nPublished: {i[3]} \nLink: {i[4]}"       
            message = client.messages.create(
                  body=msg_to_sms,
                  from_=FROM_TWILLO,
                  to=self.TO_MYNUM
                 )
            print(message.status)
       