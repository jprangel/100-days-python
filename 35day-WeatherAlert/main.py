import requests
import os
from twilio.rest import Client
from twilio.http.http_client import TwilioHttpClient
from datetime import datetime, timedelta, timezone

URL = "https://api.openweathermap.org/data/2.5/forecast"
 
MY_LAT = 55.45
MY_LONG = 37.37
FROM_TWILLO = "+19257225867"
TWILLO_ACC_ID = "AC8b9c413eaebd8bd6a525db3b07b9a3bd"
proxy_client = TwilioHttpClient()
proxy_client.session.proxies = {'https': os.environ['https_proxy']}

def set_date(in_days: int):
    """ Set the date that you want to get the weather"""
    if in_days > 5:
        print("set a date less than or equal 5 days")
        return False
    else:
        global date
        date = datetime.now(timezone.utc).date() + timedelta(days=in_days)
        return True

def set_timestamps(time_zone, in_days: int, lat, lon):
    """ Get your timestamp to filter the weather API data"""
    get_weather(lat, lon)
    global list_ts
    list_ts = []
    time = 0
    if set_date(in_days):
        for i in range(8):
            if time < 10:
                date_time = f"{date} 0{time}:00:00"
            else:
                date_time = f"{date} {time}:00:00"
            ts = datetime.strptime(date_time, '%Y-%m-%d %H:%M:%S')
            ts = ts + timedelta(hours=time_zone)
            ts = ts.timestamp()
            list_ts.append(int(ts))
            time += 3
    else:
        return False

def get_weather(lat, lon):
    """ Get the weather data in the API"""
    try:
        API_KEY = os.environ.get('WEATHER_API_KEY')
    except KeyError:
        print("Please set the environment variable")
        
    PARAM = {
        "lat": lat,
        "lon": lon,
        "appid": API_KEY,
        "exclude": "current,minutely"
    }
    
    resp = requests.get(URL, params=PARAM)
    resp.raise_for_status()
    global weather_data
    weather_data = resp.json()
    weather_data = weather_data['list']
    
def check_weather(ts, d, lat, lon):
    """ Parse the weather information and evaluate for harsh conditions"""
    is_gonna_rain = False
    try:
        set_timestamps(time_zone = ts, in_days= d, lat = lat, lon = lon)
    except:
        raise Exception("Sorry the get_timestamps is not working")
    else:
        for i in weather_data:
            if i['dt'] in list_ts:
                if i['sys']['pod'] == 'd':
                    if i['weather'][0]['id'] < 700:
                        is_gonna_rain = True
                        main = i['weather'][0]['main']
                        overall = i['weather'][0]['description']
        if is_gonna_rain:
            msg = f"Alert Harsh conditions ahead !!\nAt {date} during the day we will be mainly {main}, overall with {overall}"
            send_alert(msg)

def send_alert(msg: str):
    """ Send a text msg to your phone"""
    try:
        TO_MYNUM = os.environ.get('MY_PHONENUM')
    except KeyError:
        print("Please set the environment variable")
    try:
        auth_token = os.environ.get('TWILIO_AUTH_TOKEN')
    except KeyError:
        print("Please set the environment variable")
    
    client = Client(TWILLO_ACC_ID, auth_token, http_client=proxy_client)

    message = client.messages.create(
        body=msg,
        from_=FROM_TWILLO,
        to=TO_MYNUM
    )

    print(message.status)

# Set ts value based on your timezone, for example GMT+1 set the ts=1, set 0 for GMT
# Set d variable for the number of days ahead, limit 5, for tomorrow set 1
# Set your latitude (lat) and longitude (lon)
check_weather(ts=0, d=1, lat=53.3498, lon=6.2603)