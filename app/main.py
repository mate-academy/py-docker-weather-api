import os
import requests

from dotenv import load_dotenv

API_KEY = os.environ.get("API_KEY")
CITY = "Paris"
URL = "https://api.weatherapi.com/v1/current.json"


def get_weather() -> None:
    response = requests.get(
        "https://api.weatherapi.com/v1/current.json",
        params={
            "key": os.environ.get("API_KEY"),
            "q": "Paris"
        }
    )
    data = response.json()

    main_text = data.get("current")
    detail_text = main_text.get("condition").get("text")
    temp_c = main_text.get("temp_c")
    feelslike_c = main_text.get("feelslike_c")
    gust_kph = main_text.get("gust_kph")
    pressure_in = main_text.get("pressure_in")
    humidity = main_text.get("humidity")
    last_updated = main_text.get("last_updated")

    print(
        f"Current weather in Paris, France:\n"
        f"{detail_text}. "
        f"Temperature: {temp_c}°C, feels like {feelslike_c}°C.\n"
        f"Wind: {gust_kph} km/h \n"
        f"Humidity: {humidity}% \n"
        f"Precipitation: {pressure_in} mm \n"
        f"Last updated: {last_updated}"
    )


if __name__ == "__main__":
    get_weather()
