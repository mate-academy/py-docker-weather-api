import json
import os
import requests

API_KEY = os.environ["API_KEY"]
API_REQUEST_URL = "https://api.weatherapi.com/v1/current.json"
API_LOCATION = os.getenv("API_LOCATION", "Paris")


def get_weather() -> None:

    data = {"key": API_KEY, "q": API_LOCATION}

    response = requests.get(API_REQUEST_URL, params=data)

    received = json.loads(response.content)

    print(
        f"{'#' * 35}__WEATHER__{'#' * 35}\n"
        f"{received['location']['name']} "
        f"({received['location']['localtime']})\n"
        f"Temperature: {received['current']['temp_c']} °C\n"
        f"{received['current']['condition']['text']}\n"
        f"{'#' * 81}"
    )


if __name__ == "__main__":
    get_weather()
