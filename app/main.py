import os
from datetime import datetime, timedelta

import requests
from dotenv import load_dotenv

load_dotenv()

URL = "https://api.openweathermap.org/data/2.5/weather"
CITY = "Paris"
API_KEY = os.environ.get("WEATHER_API_KEY")


def get_weather(
        url: str = URL,
        city: str = CITY,
        api_key: str = API_KEY
) -> None:
    response = requests.get(url,
                            params={"q": city,
                                    "appid": api_key,
                                    "units": "metric"}
                            )
    if response.status_code == 200:
        data = response.json()
        current_time = (datetime.utcnow() + timedelta(
            seconds=data.get("timezone", 0)
        )).strftime("%d %B %Y - %H:%M")
        print(f"Weather information for {data['name']}, "
              f"{data['sys']['country']}:\n"
              f"current date - time: {current_time}\n"
              f"current weather: {data['weather'][0]['description']}\n"
              f"current temperature: {data['main']['temp']}C\n"
              f"feels like: {data['main']['feels_like']}C\n"
              f"humidity: {data['main']['humidity']}%\n")
    else:
        print(f"Failed to retrieve weather data. "
              f"Status Code: {response.status_code}")


if __name__ == "__main__":
    get_weather()
