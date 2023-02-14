import requests
from datetime import datetime
import time

MY_LAT = 51.507351
MY_LONG = -0.127758

def check_iss_postion():
    iss_resp = requests.get("http://api.open-notify.org/iss-now.json")
    iss_resp.raise_for_status()
    data = iss_resp.json()
    iss_long = float(data["iss_position"]["longitude"])
    iss_lat = float(data["iss_position"]["latitude"])
    print(iss_long, iss_lat)
    if MY_LAT-5 <= iss_lat <= MY_LAT+5 and MY_LONG-5 <= iss_long <= MY_LONG+5:
        return True
    
def check_nighttime():
    param = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0
    }
    resp = requests.get("https://api.sunrise-sunset.org/json", params=param)
    resp.raise_for_status()
    data = resp.json()
    sunrise = int(data['results']['sunrise'].split("T")[1].split(":")[0])
    sunset = int(data['results']['sunset'].split("T")[1].split(":")[0])
    now = datetime.now()
    if now.hour > sunset or now.hour < sunrise:
        return True

while True:
    if check_nighttime() and check_iss_postion():
        print("Look up to the sky")
    print("Sleeping 60 seconds")
    time.sleep(60)
