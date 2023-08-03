import os
import requests


URL = "http://api.weatherapi.com/v1/current.json?"
FILTERING = "Paris"


def get_weather() -> None:
    api_key = os.environ.get("API_KEY")
    url = (URL + f"key={api_key}&q={FILTERING}&lang=en")

    res = requests.get(url)

    if res.status_code != 200:
        print(f"Error: {res.status_code} - {res.reason}")
    else:
        data = res.json()
        location = data["location"]["name"]
        temperature = data["current"]["temp_c"]
        condition = data["current"]["condition"]["text"]

        print(f"The weather in {location} is {temperature}°C and {condition}.")


if __name__ == "__main__":
    get_weather()
