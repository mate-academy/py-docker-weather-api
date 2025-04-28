import requests

from settings import api_key, city

if not api_key:
    raise ValueError("API key is not set.")
if not city:
    raise ValueError("City is not set.")


def get_weather() -> None:
    weather_url = "https://api.weatherapi.com/v1/current.json"
    params = {"key": api_key, "q": city}
    response = requests.get(weather_url, params=params)
    weather_data = response.json()
    location = weather_data["location"]
    current = weather_data["current"]

    print(f"""Performing request to weather api for {city} city.
Country: {location['country']}
City: {location['name']}
District: {location['region']}
Current temperature: {current['temp_c']} °C
Feels like: {current['feelslike_c']} °C
Condition: {current['condition']['text']}
Wind: {current['wind_kph']} kph, direction {current['wind_dir']}
Humidity: {current['humidity']}%
Pressure: {current['pressure_mb']} mb
Cloudiness: {current['cloud']}%
UV Index: {current['uv']}
Local Time: {location['localtime']}
""")


if __name__ == "__main__":
    get_weather()
