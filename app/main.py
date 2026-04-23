import os

import requests


def get_weather() -> None:
    URL = "https://api.weatherapi.com/v1/current.json"
    CITY = "Paris"
    API_KEY = os.environ.get("API_KEY")
    response = requests.get(
        URL,
        params={"key": API_KEY, "q": CITY}
    )

    if response.status_code == 200:
        json_data = response.json()
        message = (
            f"{json_data['location']['country']}"
            f"/{json_data['location']['name']} "
            f"{json_data['location']['localtime']} "
            f"Weather: {json_data['current']['temp_c']} Celsius, "
            f"{json_data['current']['condition']['text']}"
        )
        print("Performing request to Weather API for city Paris...")
        print(message)
    else:
        print("An api key was not provided or invalid!")


if __name__ == "__main__":
    get_weather()
