import os
import requests


URL = "http://api.weatherapi.com/v1/current.json?"
FILTERING = "Paris"


def get_weather() -> None:
    api_key = os.environ.get("API_KEY")
    url = (URL + f"key={api_key}&q={FILTERING}&lang=en")

    response = requests.get(url)
    result = response.json()

    if result.status_code != 200:
        print(f"Error: {result.status_code} - {result.reason}")
    else:
        location = result.get("location")
        temperature = result.get("current").get("temp_c")
        condition = result.get("current").get("condition").get("text")

        if location and location.get("name"):
            location = location.get("name")

        if temperature and condition:
            print(f"Weather in {location}: {temperature}°C, {condition}")
        else:
            print("Failed to fetch weather data")


if __name__ == "__main__":
    get_weather()
