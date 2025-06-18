import requests
import os

api_key = os.environ.get("API_KEY")
URL = "http://api.weatherapi.com/v1/current.json"
CITY = "Paris"


def get_weather() -> None:
    # write your code here
    # print(URL + "key=" + api_key + "&q=" + city
    response = requests.get(
        f"{URL}?key={api_key}&q={CITY}"
    )
    print(response.json())


if __name__ == "__main__":
    get_weather()
