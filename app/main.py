import os
import requests


def get_weather() -> None:
    api_key = os.getenv("API_KEY")
    if not api_key:
        raise ValueError("API_KEY is not set in environment variables")

    url = (
        f"https://api.openweathermap.org/data/2.5/weather"
        f"?q=Paris&appid={api_key}&units=metric"
    )
    response = requests.get(url, timeout=10)
    response.raise_for_status()

    data = response.json()
    temp = data["main"]["temp"]
    weather = data["weather"][0]["description"]

    print(f"Weather in Paris: {weather}, {temp}°C")


if __name__ == "__main__":
    get_weather()
