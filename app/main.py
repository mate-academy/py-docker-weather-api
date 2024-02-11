import os
import requests
URL = "https://api.weatherapi.com/v1/current.json?"
FILTERING = "Paris"
API_KEY = os.environ.get("API_KEY")


def get_weather() -> None:
    print(f"Performing request to Weather API for city {FILTERING}...")
    result = requests.get(URL + f"q={FILTERING}&key={API_KEY}")
    if result.status_code == 200:
        data = result.json()
        location = (f"{data.get("location").get("name")}"
                    f"/{data.get("location").get("country")}")
        date = data.get("location").get("localtime")
        temperature = data.get("current").get("temp_c")
        condition = data.get("current").get("condition").get("text")
        print(f"{location} {date} Weather: {temperature} Celsius, {condition}")


if __name__ == "__main__":
    get_weather()
