import os
import requests
import dotenv
from pprint import pprint

dotenv.load_dotenv()

FILTERING = "Paris"

API_KEY = os.getenv("API_KEY")

URL = "https://api.weatherapi.com/v1/current.json"


def get_weather() -> None:
    params = {"key": API_KEY, "q": FILTERING}
    res = requests.get(URL, params=params).json()
    error = res.get("error", None)
    if error is not None:
        print(error)
        return
    location = res.get("location", {})
    current = res.get("current", {})

    weather_data = {
        "Country": location.get('country', 'N/A'),
        "City": location.get('name', 'N/A'),
        "Time": location.get('localtime', 'N/A'),
        "Weather": current.get('condition', {}).get('text', 'N/A'),
        "Temperature": f"{current.get('temp_c', 'N/A')} Celsius"
    }

    pprint(weather_data, width=1)


if __name__ == "__main__":
    get_weather()
