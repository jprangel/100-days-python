#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
from data_manager import DataManager
from flight_search import FlightSearch
from datetime import datetime, timedelta


sheet = DataManager()
flight = FlightSearch()

FROM_AIRPORT = "DUB"
found_trips = []

#data = sheet.get_info()
# Mock info from the spreadsheet, for testing purposes
data = {'prices': [{'city': 'Sao Paulo', 'iataCode': 'GRU', 'lowestPrice': 500, 'numberOfDays': 15, 'timeAhead': 180, 'directFlight': 'no', 'id': 2}, 
                   {'city': 'Cluj', 'iataCode': 'CLJ', 'lowestPrice': 150, 'numberOfDays': 3, 'timeAhead': 90, 'directFlight': 'yes', 'id': 3}]}

def get_date(num_days = 0):
    date = datetime.now().date() + timedelta(days=num_days)
    return (date.strftime("%d/%m/%Y"), date.strftime('%A'))

for l in data['prices']:
    to_airport = l['iataCode']
    date_from = get_date(num_days=l['timeAhead'])
    date_to = get_date(num_days=l['timeAhead']+15)
    if l['directFlight'] == "yes":
        stop = 0
    else:
        stop = 2
    info = flight.search_flight(f_from=FROM_AIRPORT, f_to=to_airport, 
                                f_date_from=date_from[0], f_date_to=date_to[0], 
                                nights_in_dst_to=l['numberOfDays'], stopsover=stop)
    print(f"Searching from {FROM_AIRPORT} to {to_airport} / Range of dates: {date_from} to {date_to} / At price lowest than: {l['lowestPrice']}")
    no_lowest_price = True
    for i in info['data']:
        if i['conversion'][flight.currency] < l['lowestPrice']:
            no_lowest_price = False
            trips = []
            for r in i['route']:
                dict = {
                    'from': r['cityFrom'],
                    'to': r['cityTo'],
                    'utc_departure': r['utc_departure'],
                    'utc_arrival': r['utc_arrival']
                }
                
                trips.append(dict)
            chars = { 
                     'seats' : i['availability']['seats'],
                     'price': i['conversion'][flight.currency]
                    }
            trips.append(chars)
            found_trips.append(trips)
    if no_lowest_price:
        print("No lowest price found for this trip")
# Mock expected output
""" [
    {
        'routes': [
            {'from': 'Dublin', 'to': 'Cluj-Napoca', 'utc_departure': '2023-05-28T19:50:00.000Z', 'utc_arrival': '2023-05-28T22:50:00.000Z'}, 
            {'from': 'Cluj-Napoca', 'to': 'Dublin', 'utc_departure': '2023-05-31T18:30:00.000Z', 'utc_arrival': '2023-05-31T21:50:00.000Z'}
        ],
        'items': [
            {'seats': 4, 'price': 147}
        ]
    },

    {
        'routes': [
            {'from': 'Dublin', 'to': 'Cluj-Napoca', 'utc_departure': '2023-05-31T22:50:00.000Z', 'utc_arrival': '2023-06-01T01:50:00.000Z'}, 
            {'from': 'Cluj-Napoca', 'to': 'Dublin', 'utc_departure': '2023-06-04T15:00:00.000Z', 'utc_arrival': '2023-06-04T18:20:00.000Z'}
        ],
        'items': [
            {'seats': 2, 'price': 147}
        ]
    }
] """

if found_trips.__len__() > 0 :
    for i in found_trips:
        for x in i:
            msg = f"{x['from']} {x['to']} {x['utc_departure']} {x['utc_arrival']}"
             
        #msg = f"{x['seats']} {x['price']}"
        #print(msg)
