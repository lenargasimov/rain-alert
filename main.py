import os
import requests

OWM_Endpoint = 'https://api.openweathermap.org/data/2.5/onecall'
api_key = os.environ.get('API_KEY')

weather_params = {
    "lat": 55.766334,
    "lon": 52.460639,
    "appid": api_key,
}

response = requests.get(OWM_Endpoint, params=weather_params)
print(response.json())