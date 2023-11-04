import requests
from twilio.rest import Client

account_sid = 'ACef40a40b63f100deb278fed2966ad11d'                                                       # Twilio account_sid
auth_token = 'f707963d20349e6d497deb5566093356'                                                          # Twilio auth_token

api_key = "b3d83a7a964b9186d658d70725650027"                                                             # OpenWeatherMap API key
OWM_API_Endpoint = "https://api.openweathermap.org/data/2.5/weather"                                     # OpenWeatherMap API End point

parameters = {
    "q": "Buea",
    "appid": api_key,
}

response = requests.get(OWM_API_Endpoint, params=parameters)
response.raise_for_status()    # This allows the response to raise an exception in case of errors

weather_data = response.json()['weather'][0]

weather_id = weather_data["id"]

if weather_id <= 700:
    client = Client(account_sid, auth_token)        # Twilio account_sid and auth_token

    message = client.messages.create(
        body="It is going to rain today. Please take an umbrella ☂️",
        from_="+17406192975",
        to="+14377708882"
    )
    print(message.status)

