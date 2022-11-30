from dotenv import load_dotenv
import os
import requests


load_dotenv()

URL = "https://api.weatherapi.com/v1/current.json"
API_KEY = os.getenv("API_KEY")
CITY = "London"


def get_weather() -> None:
    response = requests.get(
        URL,
        params={"key": API_KEY, "q": CITY},
    ).json()
    city = response["location"]["name"]
    country = response["location"]["country"]
    temp = response["current"]["temp_c"]
    date = response["location"]["localtime"]
    condition = response["current"]["condition"]["text"]
    print(
        f"City: {city}, Country: {country}, "
        f"Temperature: {temp}, Date: {date}, Condition: {condition}"
    )


if __name__ == "__main__":
    get_weather()
