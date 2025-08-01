import os
import requests

api_key = os.getenv("API_KEY")
city = "Paris"
url = f"http: //api.weatherapi.com/v1/current.json?key={api_key}&q={city}&aqi=no"

response = requests.get(url)
data = response.json()

weather = data["current"]["condition"]["text"]
temp_c = data["current"]["temp_c"]
local_time = data["location"]["localtime"]

print(f"{city}/France {local_time} Weather: {temp_c} Celsius, {weather}")
