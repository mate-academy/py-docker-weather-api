import os
import requests


BASE_URL = "http://api.weatherapi.com/v1/current.json"
CITY = "Paris"
LANG = "en"


def get_weather() -> None:
    api_key = os.getenv("API_KEY")
    if not api_key:
        print("Error: API_KEY not found in environment")
        return

    params = {
        "key": api_key,
        "q": CITY,
        "lang": LANG
    }

    response = requests.get(BASE_URL, params=params)
    if response.status_code == 200:
        data = response.json()
        location = data["location"]
        current = data["current"]
        print(f"{location["name"]}/{location["country"]} "
              f"{location["localtime"]} | "
              f"Weather: {current["temp_c"]} Celsius, "
              f"{current["condition"]["text"]}")
    else:
        print("Error:", response.status_code)


if __name__ == "__main__":
    get_weather()
