import requests
from twilio.rest import Client


API_KEY = "09f32e5efe5eca70dee1890c9fc0f10f"
LON = -63.179162
LAT = -17.783279
account_sid = "ACa5e6b2711d15254d3e8db1fc0f1f2676"
auth_token = "debc57cab4da67ad41d6e2eaf05afd0c"
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

