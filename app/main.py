import os
from dotenv import load_dotenv
import requests

load_dotenv()
URL = "https://api.weatherapi.com/v1/current.json?"
FILTERING = "Paris"
API_KEY = os.getenv("API_KEY")


def get_weather() -> None:
    response = requests.get(URL + "key=" + API_KEY + f"&q={FILTERING}")
    if response.status_code == 200:
        response = response.json()
        location = response["location"]
        current = response["current"]
        # Print the content of the response, which should be the weather data
        print(f"{location['name']}/{location['country']} "
              f"{location['localtime']} "
              f"Weather: {current['temp_c']} Celsius, "
              f"{current['condition']['text']}")
    else:
        # If the response was not successful, print an error message
        print("Failed to get data, status code:", response.status_code)

    # Check the status code of the response to make sure it was successful


if __name__ == "__main__":
    get_weather()
