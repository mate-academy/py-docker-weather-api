import os

import requests

URL = "http://api.weatherapi.com/v1/current.json"
API_KEY = os.environ.get("API_KEY")
CITY = "Paris"


def get_weather() -> None:
    if not API_KEY:
        print("Error: API_KEY not set!")
        return

    params = {
        "key": API_KEY,
        "q": CITY
    }
    response = requests.get(URL, params=params)

    if response.status_code == 200:
        data = response.json()
        print(f"Weather in {data['location']['name']},"
              f" {data['location']['country']}:")
        print(f"Temperature: {data['current']['temp_c']}°C")
        print(f"Condition: {data['current']['condition']['text']}")
        print(f"Wind Speed: {data['current']['wind_kph']}")
    else:
        print(f"Error: {response.status_code}  - {response.text}")


if __name__ == "__main__":
    get_weather()
