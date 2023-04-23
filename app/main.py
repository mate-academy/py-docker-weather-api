import requests
import os
from dotenv import load_dotenv

load_dotenv()


def get_weather() -> str:
    key = os.environ.get("KEY")
    filtering = "Paris"
    url = "http://api.weatherapi.com/v1/current.json?key="
    response = requests.get(url + f"{key}&q=" + f"{filtering}&api=no")
    weather_data = response.json()
    temperature = weather_data.get("current")["temp_c"]
    return f"The temperature in {filtering} is {temperature} degrees Celsius"


if __name__ == "__main__":
    print(get_weather())
