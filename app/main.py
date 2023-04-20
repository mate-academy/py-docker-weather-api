import os
import requests
# 3e82112350fd46cd8d954441231404

LOCATION = "Paris"
API_KEY = os.getenv("API_KEY")


def get_weather() -> None:
    url = "https://api.weatherapi.com/v1/current.json"

    params = {
        "key": API_KEY,
        "q": LOCATION,
    }

    response = requests.get(url, params=params)

    print(response.content)


if __name__ == "__main__":
    get_weather()
