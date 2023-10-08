import os
import dotenv
import requests

dotenv.load_dotenv()

CURRENT_WEATHER_URL = "https://api.weatherapi.com/v1/current.json"
FILTER = "Paris"
WEATHER_API_KEY = os.getenv("API_KEY")


def get_weather() -> None:
    query_param = {
        "key": WEATHER_API_KEY,
        "q": FILTER
    }

    response = requests.get(CURRENT_WEATHER_URL, params=query_param)

    if response.status_code == 200:
        data = response.json()

        country = data["location"]["country"]
        city = data["location"]["name"]
        last_updated = data["current"]["last_updated"]

        temp_cels = data["current"]["temp_c"]
        temp_fahren = data["current"]["temp_f"]

        weather = data["current"]["condition"]["text"]
        humidity = data["current"]["humidity"]
        wind = data["current"]["wind_kph"]

        print(
            f"{country}/{city} {last_updated}"
            f" Weather: {weather}, {temp_cels} Celsius /"
            f" {temp_fahren} Fahrenheit,"
            f" Humidity: {humidity}%,"
            f" Wind: {wind} km/hr"
        )


if __name__ == "__main__":
    get_weather()
