import os
import requests


URL = "http://api.weatherapi.com/v1/current.json?"
FILTERING = "Paris"


def get_weather() -> None:
    api_key = os.environ.get("API_KEY")
    url = (URL + f"key={api_key}&q={FILTERING}&lang=en")

    result = requests.get(url)

    if result.status_code != 200:
        print(f"Error: {result.status_code} - {result.reason}")
    else:
        data = result.json()
        location = data["location"]["name"]
        temperature = data["current"]["temp_c"]
        condition = data["current"]["condition"]["text"]

        print(f"The weather in {location} is {temperature}°C and {condition}.")


if __name__ == "__main__":
    get_weather()
