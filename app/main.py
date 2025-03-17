import os
import requests

URL = "https://api.weatherapi.com/v1/current.json"
API_KEY = os.getenv("API_KEY")
Q_param = os.getenv("Q", "Paris")


def get_weather() -> None:
    params = {
        "key": API_KEY,
        "q": Q_param,
    }
    response = requests.get(URL, params=params)
    if response.status_code == 200:
        location = response.json()["location"]
        country = location["country"]
        city = location["name"]

        current = response.json()["current"]
        time = current["last_updated"]
        temp_c = current["temp_c"]
        condition = current["condition"]["text"]

        print(
            f"{city}/{country} {time} Weather: {temp_c} Celsius, {condition}"
        )
    else:
        raise Exception(response.status_code)


if __name__ == "__main__":
    get_weather()
