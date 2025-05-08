import requests
import os


def get_weather() -> None:
    API_KEY = os.getenv("API_KEY")

    if not API_KEY:
        raise Exception("API_KEY not found in environment")

    CITY = "Paris"
    URL = (f"https://api.openweathermap.org/data/2.5/weather?q="
           f"{CITY}&appid={API_KEY}&units=metric")

    response = requests.get(URL)

    if response.status_code == 200:
        data = response.json()
        print(f"Current temperature in {CITY} is {data['main']['temp']}°C")
    else:
        print(f"Failed to get weather data for {CITY}")


if __name__ == "__main__":
    get_weather()
