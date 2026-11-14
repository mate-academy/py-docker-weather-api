import os
import requests

API_URL = "https://api.openweathermap.org/data/2.5/weather"
CITY = "Paris"


def get_weather() -> None:
    api_key = os.getenv("API_KEY")
    if not api_key:
        print("Error: API_KEY environment variable is missing!")
        return

    url = f"{API_URL}?q={CITY}&appid={api_key}&units=metric"

    try:
        response = requests.get(url)
        data = response.json()

        if response.status_code == 200:
            temp = data["main"]["temp"]
            desc = data["weather"][0]["description"]
            print(f"Weather in {CITY}: {temp}°C, {desc}")
        else:
            msg = data.get("message", "Unknown error")
            print(f"Failed to fetch weather: {msg}")

    except Exception as e:
        print(f"An error occured: {e}")


if __name__ == "__main__":
    get_weather()
