import os
import requests
from dotenv import load_dotenv


CITY = "Paris"
CURRENT_WEATHER_API_URL = "http://api.weatherapi.com/v1/current.json"


def get_weather() -> None:
    load_dotenv()
    api_key = os.environ.get("API_KEY")

    if not api_key:
        print("Error: API_KEY not found in environment variables.")
        return

    payload = {
        "key": api_key,
        "q": CITY
    }
    res = requests.get(CURRENT_WEATHER_API_URL,
                       params=payload
                       )
    res.raise_for_status()
    data = res.json()
    print(f"Here is information about the current weather in "
          f"{data['location']['name']}, {data['location']['country']}:")
    print(f"Air temperature is {data['current']['temp_c']}C "
          f"which feels like {data['current']['feelslike_c']}C")
    print(f"It is {data['current']['condition']['text']}")
    print(f"Humidity is {data['current']['humidity']}%")
    print(f"Wind speed is {data['current']['wind_kph']} km/h "
          f"with {data['current']['wind_dir']} direction")
    print(f"Cloud cover is {data['current']['cloud']}%")
    print(f"UV Index is {data['current']['uv']}")
    print(f"This was last updated {data['current']['last_updated']}")


if __name__ == "__main__":
    get_weather()
