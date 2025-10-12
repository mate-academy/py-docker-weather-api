import os
import requests

def get_weather() -> None:
    api_key = os.getenv("WEATHER_API_KEY")
    if not api_key:
        print("Error: didn't find WEATHER_API_KEY in environment variables.")
        return

    city = "Paris"
    url = f"http://api.weatherapi.com/v1/current.json?key={api_key}&q={city}&lang=en"

    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        location = data["location"]
        current = data["current"]
        print(f"{location['name']}/{location['country']} {location['localtime']} | "
              f"Weather: {current['temp_c']} Celsius, {current['condition']['text']}")
    else:
        print("Error:", response.status_code)


if __name__ == "__main__":
    get_weather()