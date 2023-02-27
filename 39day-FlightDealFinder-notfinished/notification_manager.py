from twilio.rest import Client
from conn import Conn

class NotificationManager:
    #This class is responsible for sending notifications with the deal flight details.
    
    def __init__(self) -> None:
        self.conn = Conn()
    
    def send_alert(self):
        pass