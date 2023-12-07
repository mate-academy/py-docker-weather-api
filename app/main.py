import requests
import os

API_KEY = os.environ.get("API_KEY")
URL = "http://api.weatherapi.com/v1/current.json"
CITY = "Paris"


def get_weather() -> None | dict:
    params = {"key": API_KEY, "q": CITY}
    print("Performing request to Weather API for city Paris...")
    response = requests.get(URL, params=params)
    if response.status_code == 200:
        return response.json()
    print(f"Error occurred, response status code: {response.status_code}")
    return None


if __name__ == "__main__":
    weather_data = get_weather()
    if weather_data:
        print(
            f"{weather_data['location']['name']}/{weather_data['location']['country']} "
            f"{weather_data['location']['localtime']} "
            f"Weather: {weather_data['current']['temp_c']} Celsius, "
            f"{weather_data['current']['condition']['text']}"
        )
