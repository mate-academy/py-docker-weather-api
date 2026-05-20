import os
import requests

from dotenv import load_dotenv


load_dotenv()

URL = "http://api.weatherapi.com/v1/current.json"
FILTERING = "Paris"


def get_weather() -> None:
    params = {
        "key": os.getenv("API_KEY"),
        "q": FILTERING,
    }

    result = requests.get(URL, params=params)

    if result.status_code == 200:
        data = result.json()

        city = data["location"]["name"]
        country = data["location"]["country"]
        temp = data["current"]["temp_c"]
        condition = data["current"]["condition"]["text"]

        print(f"Weather for {city}, {country}")
        print(f"Temperature: {temp}°C")
        print(f"Condition: {condition}")

    else:
        print(f"Error: {result.status_code}")
        print(result.text)


if __name__ == "__main__":
    get_weather()
