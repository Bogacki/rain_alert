import requests
from twilio.rest import Client


API_KEY = "a4da4e1478f06ef5337093adf0806f7f"
account_sid = "ACb13e6cebfba1bbfe681f23dabb11f201"
auth_token = "39c64c39a6457134bc68c0d07eb3f0eb"


weather_parameters = {
    "lat":52.406376,
    "lon":16.925167,
    "exclude":"current,minutely,daily",
    "appid": API_KEY,
}

response = requests.get(url=f"https://api.openweathermap.org/data/2.5/onecall", params=weather_parameters)
data = response.json()

weather_for_next_half_day = data["hourly"][:12]

will_rain = False

for hour_data in weather_for_next_half_day:
    for weather_condition in hour_data["weather"]:
        if weather_condition["id"] < 700:
            will_rain = True

if will_rain:

    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
        body="Take umbrella with you ☂️",
        from_='+12242617803',
        to='+48510231407'
    )
else:
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
        body="Today, you don't need ☂",
        from_='+12242617803',
        to='+48510231407'
    )