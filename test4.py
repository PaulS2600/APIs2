import json
import pandas as pd
import requests
# Frenchay Stop C
URL4 = 'https://transportapi.com/v3/uk/bus/stop_timetables/0170SGP90684.json?app_id=34667bc7&app_key=d6c0783b395f3773e1a52761360ed906'
response = requests.get(URL4)
data = response.json()

departures = (data['departures']['all'])

df = pd.DataFrame(departures)

df = df.drop(columns=['id', 'mode', 'line', 'operator', 'aimed', 'expected_departure_date', 'expected_departure_time', 'expected'])
print (df)
#print(data)
