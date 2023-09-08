import requests
import pandas as pd
from datetime import datetime

# Fetch the data from the USGS API
response = requests.get("https://earthquake.usgs.gov/fdsnws/event/1/query?format=geojson&orderby=magnitude&limit=5")
data = response.json()

# Extract the relevant data
earthquake_list = []

for earthquake in data["features"]:
    magnitude = earthquake["properties"]["mag"]
    time_millis = earthquake["properties"]["time"]
    time_readable = datetime.utcfromtimestamp(time_millis/1000).strftime('%Y-%m-%d %H:%M:%S')
    latitude = earthquake["geometry"]["coordinates"][1]
    longitude = earthquake["geometry"]["coordinates"][0]
    place = earthquake["properties"]["place"]
    
    earthquake_list.append([magnitude, time_readable, latitude, longitude, place])

# Convert the list to a pandas DataFrame
df = pd.DataFrame(earthquake_list, columns=['Magnitude', 'Time', 'Latitude', 'Longitude', 'Place'])

# Save the DataFrame to a CSV file
df.to_csv("earthquakes.csv", index=False)
