import os
import requests


BASE_URL = "http://api.weatherapi.com/v1/current.json"
CITY = "Paris"


def get_weather() -> None:
    api_key = os.getenv("API_KEY")
    if not api_key:
        raise ValueError("API_KEY environment variable is not set!")

    params = {
        "key": api_key,
        "q": CITY
    }
    response = requests.get(BASE_URL, params=params)

    response = requests.get(BASE_URL, params=params)
    response.raise_for_status()

    data = response.json()
    location = data["location"]["name"]
    country = data["location"]["country"]
    local_time = data["location"]["localtime"]
    temp_c = data["current"]["temp_c"]
    condition = data["current"]["condition"]["text"]

    output_string = (
        f"{location}/{country} {local_time} "
        f"Weather: {temp_c} Celsius, {condition}"
    )
    print(output_string)


if __name__ == "__main__":
    get_weather()
