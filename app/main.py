import os
import requests

from dotenv import load_dotenv


load_dotenv()


URL = "http://api.weatherapi.com/v1/current.json"
FILTERING = "Paris"
API_KEY = os.getenv("API_KEY", None)


def get_weather() -> None:
    params = {
        "key": API_KEY,
        "q": FILTERING,
    }
    try:
        result = requests.get(URL, params=params)
        data = result.json()

        location_city = data.get("location").get("name")
        location_country = data.get("location").get("country")

        last_updated = data.get("current").get("last_updated")
        temperature = data.get("current").get("temp_c")
        weather_description = (data.get("current")
                               .get("condition").get("text"))

        print(
            f"{location_city}/{location_country} "
            f"{last_updated} Weather: {temperature} "
            f"Celsius, {weather_description}"
        )
    except Exception as error:
        print(f"Error: {error}")


if __name__ == "__main__":
    get_weather()
