import os
import requests


def get_weather():
    city = "Paris"
    api_key = os.environ["API_KEY"]
    payload = {
        "key": api_key,
        "q": city
    }
    url = "http://api.weatherapi.com/v1/current.json"

    print(f"Performing request to Weather Api for city {city}...")

    response = requests.get(url, params=payload)
    response_data = response.json()

    returned_city = response_data["location"]["name"]
    country = response_data["location"]["country"]
    time = response_data["location"]["localtime"]
    temperature = response_data["current"]["temp_c"]
    condition = response_data["current"]["condition"]["text"]

    print(
        f"{returned_city}/{country} {time} "
        f"Weather: {temperature} Celsius, {condition}"
    )


if __name__ == "__main__":
    get_weather()
