import requests

URL = "https://opentdb.com/api.php"
PARAM = {
    "amount": 10,
    "type": "boolean",
    "category": 18
}

resp = requests.get(URL, params=PARAM)
resp.raise_for_status()
question_data = resp.json()
question_data = question_data['results']