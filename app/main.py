import os

import requests


URL = "http://api.weatherapi.com/v1/current.json"
API_KEY = os.getenv("API_KEY")
LOCATION = "Paris"


def get_weather() -> None:
    url = URL
    payload = {
        "key": API_KEY,
        "q": LOCATION,
    }
    res = requests.get(
        url=url,
        params=payload,
    )

    res_json = res.json()

    location = res_json["location"]["name"]
    country = res_json["location"]["country"]
    local_time = res_json["location"]["localtime"]
    temp_celsius = res_json["current"]["temp_c"]
    condition = res_json["current"]["condition"]["text"]

    result = (
        f"{location}/{country} "
        f"{local_time} "
        f"Weather: "
        f"{temp_celsius} Celsius, "
        f"{condition}"
    )
    print(result)


if __name__ == "__main__":
    get_weather()
