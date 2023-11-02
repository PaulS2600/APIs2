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

# College Road
URL5 = 'https://transportapi.com/v3/uk/bus/stop_timetables/0100BRA10560.json?app_id=34667bc7&app_key=d6c0783b395f3773e1a52761360ed906'
response2 = requests.get(URL5)
data2 = response2.json()
departures2 = (data2['departures']['all'])
df2 = pd.DataFrame(departures2)
df2 = df2.drop(columns=['id', 'mode', 'line', 'operator', 'aimed', 'expected_departure_date', 'expected_departure_time', 'expected'])
print (df2)


