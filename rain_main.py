import os

import requests
from twilio.rest import Client


API_KEY = os.environ.get('apik')
LON = -63.179162
LAT = -17.783279
account_sid = os.environ.get('acc_sid')
auth_token = os.environ.get('acc_t')
parameter = {
    "lat": LAT,
    "lon": LON,
    "appid": API_KEY,
    "cnt": 4
}

response = requests.get(url="https://api.openweathermap.org/data/2.5/forecast", params=parameter)
response.raise_for_status()
weather_data = response.json()
print(weather_data)
will_rain = False
for i in range(len(weather_data["list"])):
    weather_id = weather_data["list"][i]["weather"][0]["id"]
    if weather_id < 700:
        will_rain = True
if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body="It's going to rain today. Remember to bring an umbrella",
        from_="+15077055194",
        to="+919342623761",
    )
    print(message.status)

