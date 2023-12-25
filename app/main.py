import os
import requests

CITY = "Paris"
URL = "http://api.weatherapi.com/v1/current.json"
API_KEY = os.environ.get("API_KEY")


def get_weather() -> None:
    response = requests.get(URL, params={"q": CITY, "key": API_KEY})
    response.raise_for_status()

    data = response.json().get("current")
    temp_c, feelslike_c, date_and_time, descriptions = (
        data.get("temp_c"),
        data.get("feelslike_c"),
        data.get("last_updated"),
        data["condition"]["text"],
    )
    print(
        f"City: {CITY}\n"
        f"As of: {date_and_time}\n"
        f"Temperature: {temp_c}\n"
        f"Celsius Feels like in Celsius: {feelslike_c}\n"
        f"Weather description: {descriptions}"
    )


if __name__ == "__main__":
    get_weather()
