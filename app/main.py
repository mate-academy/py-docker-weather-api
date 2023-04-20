import requests
import os


URL = "https://api.weatherapi.com/v1/current.json?"
FILTERING = "Paris"
API_KEY = os.environ.get("API_KEY")


def get_weather() -> None:
    res = requests.get(URL, params={"key": API_KEY, "q": FILTERING})
    print(res.content)


if __name__ == "__main__":
    get_weather()
