import os
from dotenv import load_dotenv

import requests


load_dotenv()


def get_weather() -> None:
    api_key = os.getenv("API_KEY")
    location = os.getenv("LOCATION")

    if not api_key:
        print("Error: environment variable API_KEY is missing.")
        exit(1)

    if not location:
        print("Error: environment variable LOCATION is missing.")
        exit(1)

    url = (f"http://api.weatherapi.com/v1/"  # noqa: E231
           f"current.json?key={api_key}&q={location}&aqi=no")

    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()

        location_name = data["location"]["name"]
        country = data["location"]["country"]
        temp_c = data["current"]["temp_c"]
        condition = data["current"]["condition"]["text"]

        print(f"Weather in {location_name}, {country}:")  # noqa: E231
        print(f"Temperature: {temp_c}°C")
        print(f"Condition: {condition}")

    except requests.RequestException as e:
        print(f"Request error: {e}")
    except KeyError:
        print("Error parsing data. "
              "Possibly an invalid API key or unexpected response format.")


if __name__ == "__main__":
    get_weather()
