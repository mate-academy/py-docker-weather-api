import os
import requests


def get_weather(city: str) -> None:
    API_KEY = os.getenv("API_KEY")
    if not API_KEY:
        raise ValueError("API_KEY environment variable not set")

    URL = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"

    try:
        response = requests.get(URL)
        response.raise_for_status()
        data = response.json()
        temp = data["main"]["temp"]
        print(f"Current temperature in {city}: {temp}°C")
    except requests.exceptions.RequestException as e:
        print(f"Error fetching weather: {e}")
    except KeyError:
        print("Invalid response received from weather API")


if __name__ == "__main__":
    city = os.getenv("CITY", "London")  # Default to London if not specified
    get_weather(city)