import json
import pandas as pd
import openpyxl
# Open local json file for testing
with open('response.json', 'r') as file:
    data = json.load(file)

departures = (data['departures']['all'])

df = pd.DataFrame(departures)

#print (df)
#df.to_excel('output2.xlsx', index=False, engine='openpyxl')
#print (departures)

df = df.drop(columns=['id', 'mode', 'line', 'operator', 'aimed', 'expected_departure_date', 'expected_departure_time', 'expected'])
print (df)
             