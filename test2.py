import requests
import json
import pandas as pd
import openpyxl

# Just URL testing
URL1 = 'https://transportapi.com/v3/uk/bus/stop_timetables/0100BRA10560.json?app_id=34667bc7&app_key=d6c0783b395f3773e1a52761360ed906&datetime=2023-10-30T09:00:00+01:00&from_offset=PT00:00:00&limit=20&live=false&to_offset=PT10:00:00'
URL2 = 'https://transportapi.com/v3/uk/bus/stop_timetables/0100BRA10560.json?app_id=34667bc7&app_key=d6c0783b395f3773e1a52761360ed906&limit=20&live=false&to_offset=PT10:00:00'
URL3 = 'https://transportapi.com/v3/uk/bus/stop_timetables/450024834.json?app_id=34667bc7&app_key=d6c0783b395f3773e1a52761360ed906&limit=20&live=false&to_offset=PT10:00:00'

# Frenchay Stop C
URL4 = 'https://transportapi.com/v3/uk/bus/stop_timetables/0170SGP90684.json?app_id=34667bc7&app_key=d6c0783b395f3773e1a52761360ed906'

# College Road
URL5 = 'https://transportapi.com/v3/uk/bus/stop_timetables/0100BRA10560.json?app_id=34667bc7&app_key=d6c0783b395f3773e1a52761360ed906'

# Logndown Ave
URL6 = 'https://transportapi.com/v3/uk/bus/stop_timetables/017000017.json?app_id=34667bc7&app_key=d6c0783b395f3773e1a52761360ed906'

# LiveTrue Test
URL7 = 'https://transportapi.com/v3/uk/bus/stop_timetables/017000017.json?app_id=34667bc7&app_key=d6c0783b395f3773e1a52761360ed906&live=true&source_config=tnds'

# 48a information test
URL8 = 'https://transportapi.com/v3/uk/bus/services/FBRO:048A.json?app_id=34667bc7&app_key=d6c0783b395f3773e1a52761360ed906'

response = requests.get(URL6)

#if response.status_code == 200:
data = response.json()

output_filename = "response4.json"
with open(output_filename, "w") as file:
    json.dump(data, file, indent=4)

#print(f"da file is written to {output_filename}")

#formatted_data = json.dumps(data, indent=4)

# print(data['smscode'])
# print(formatted_data)

# stuff = pd.DataFrame(data)
# print(stuff)

# df = pd.DataFrame(data)
# print(df.head(2))
#data2 = pd.json_normalize(data)
#print(data2)

df = pd.DataFrame(data)
#df.to_excel('output.xlsx', index=False, engine='openpyxl')

print(df['all'])




