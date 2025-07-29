import requests
import os
from dotenv import load_dotenv


URL = "https://api.weatherapi.com/v1/current.json?"
FILTERING = "Paris"
load_dotenv()
API_KEY = os.getenv("API_KEY")


def get_weather() -> None:
    response = requests.get(URL + f"q={FILTERING}&key={API_KEY}").json()

    city_name = response.get("location").get("name")
    country_name = response.get("location").get("country")
    local_datetime = response.get("location").get("localtime")
    temp_c = response.get("current").get("temp_c")
    weather_condition = response.get("current").get("condition").get("text")
    print(
        f"{city_name}/{country_name} {local_datetime}"
        f" Weather: {temp_c} Celsius, {weather_condition}"
    )


if __name__ == "__main__":
    get_weather()
