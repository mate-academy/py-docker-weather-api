import requests
import os
from dotenv import load_dotenv


load_dotenv()

API_KEY = os.getenv("API_KEY")
CITY = "Paris"
URL = f"http://api.weatherapi.com/v1/current.json?key={API_KEY}&q={CITY}"


def get_weather() -> None:
    if not API_KEY:
        print("API key not found")
        return

    response = requests.get(URL)
    if response.status_code == 200:
        data = response.json()
        print(f"Weather in {CITY}: {data['current']['temp_c']}°C, "
              f"{data['current']['condition']['text']}")
    else:
        print(f"Error: {response.status_code}, {response.text}")


if __name__ == "__main__":
    get_weather()
