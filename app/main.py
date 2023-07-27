import os
import requests


API_KEY = os.environ.get("API_KEY")
BASE_URL = "https://api.weatherapi.com/v1"
CITY = "Paris"


def get_weather() -> None:
    response = requests.get(
        BASE_URL + "/current.json",
        params={"key": API_KEY, "q": CITY}
    )
    data_json = response.json()

    if response.status_code == 200:
        location = data_json.get("location")
        current = data_json.get("current")
        print(
            f"{location.get('country')} - {location.get('name')}\n"
            f"Current time: {location.get('localtime').split()[1]}\n"
            f"Temperature: {current.get('temp_c')} ℃\n"
            f"Condition: {current.get('condition').get('text')}"
        )


if __name__ == "__main__":
    get_weather()
