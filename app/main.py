import os
import requests

API_KEY = os.getenv("API_KEY")
CITY = os.getenv("CITY", "Paris")
BASE_URL = "http://api.weatherapi.com/v1/current.json"


def get_weather() -> None:
    if not API_KEY:
        raise ValueError("NO API_KEY! Set -e API_KEY=<your_api_key>")

    url = f"{BASE_URL}?key={API_KEY}&q={CITY}"
    response = requests.get(url)
    response.raise_for_status()
    data = response.json()

    cond = data["current"]["condition"]["text"]
    temperature_c = data["current"]["temp_c"]
    print(f"Weather in {CITY}: {cond}, {temperature_c}°C")
    return None


if __name__ == "__main__":
    get_weather()
