import requests
import os


def get_weather() -> str:

    API_KEY = os.environ.get("API_KEY")
    CITY = "Paris"

    url = f"http://api.weatherapi.com/v1/current.json?key={API_KEY}&q={CITY}&lang=en"

    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        location = data["location"]["name"]
        temp = data["current"]["temp_c"]
        condition = data["current"]["condition"]["text"]
        return f"Weather in {location}: {condition}, {temp}°C"


if __name__ == "__main__":
    print(get_weather())
