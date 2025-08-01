import os
import requests

API_KEY = os.getenv("API_KEY")
CITY = "Paris"
URL = f"http://api.weatherapi.com/v1/current.json?key={API_KEY}&q={CITY}&aqi=no"

response = requests.get(URL)
data = response.json()

weather = data["current"]["condition"]["text"]
temp_c = data["current"]["temp_c"]
local_time = data["location"]["localtime"]

print(f"{CITY}/France {local_time} Weather: {temp_c} Celsius, {weather}")
