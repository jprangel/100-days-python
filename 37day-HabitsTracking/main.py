import requests
import os
from datetime import datetime

ENDPOINT = "https://pixe.la/v1"
TOKEN = os.environ['PIXELA_TOKEN']
USERNAME = "jprangel"
ID_GRAPH = "dog-walk"
HEADER = { "X-USER-TOKEN": TOKEN }

def create_user():
    create_user_json = { 
        "token": TOKEN, 
        "username": USERNAME, 
        "agreeTermsOfService":"yes", 
        "notMinor":"yes"
    }
    CREATE_USER_API = f"{ENDPOINT}/users"
    r = requests.post(url=CREATE_USER_API, json=create_user_json)
    print(r.text)

def create_graph():
    create_graph_json = {
        "id": ID_GRAPH,
        "name":"daily dog walk",
        "unit":"steps",
        "type":"int",
        "color":"momiji"
    }
    CREATE_GRAPH_API = f"{ENDPOINT}/users/{USERNAME}/graphs"
    r = requests.post(url=CREATE_GRAPH_API, json=create_graph_json, headers=HEADER)
    print(r.text)

def update_graph(date: str,qntd: str):
    update_graph_json = {
        "date": date,
        "quantity": qntd
    }
    UPDATE_GRAPH_API = f"{ENDPOINT}/users/{USERNAME}/graphs/{ID_GRAPH}"
    r = requests.post(url=UPDATE_GRAPH_API, json=update_graph_json, headers=HEADER)
    print(r.text)
    
def get_date():
    today = datetime.now().date()
    return today.strftime("%Y%m%d")

#create_user()
#create_graph()

steps = input("How many steps did you do today with the dog 🐶? ")
update_graph(get_date(), steps)
