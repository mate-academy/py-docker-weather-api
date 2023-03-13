import os
import requests
from dotenv import load_dotenv

load_dotenv()


def get_weather() -> None:
    response = requests.get(URL, PARAMS).json()
    location = response["location"]
    weather = response["current"]

    print(
        f"""
    Weather report in {location["name"]}, {location["country"]}.
    Temperature is {weather["temp_c"]}°C. Feels like {weather["feelslike_c"]}.
    Condition: {weather["condition"]["text"]}.
    Wind report:
        Speed is {weather["wind_kph"]} km/h (gusts to {weather["gust_kph"]}),
        Direction is {weather["wind_dir"]} ({weather["wind_degree"]}°).
    Pressure is {weather["pressure_mb"]} hPa.
    Humidity is {weather["humidity"]}%.
    Visibility is {weather["vis_km"]} kilometres.
    """
    )


if __name__ == "__main__":
    API_KEY = os.environ["API_KEY"]
    URL = "http://api.weatherapi.com/v1/current.json"
    FILTERING = "Paris"
    PARAMS = {"key": API_KEY, "q": FILTERING}

    get_weather()
