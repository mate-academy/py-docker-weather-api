import os
import requests


def get_weather() -> None:
    api_key = os.getenv("API_KEY")
    if not api_key:
        raise ValueError("API_KEY environment variable is not set")

    url = "http://api.weatherapi.com/v1/current.json"
    params = {
        "key": api_key,
        "q": "Paris"
    }

    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        weather_data = response.json()
        print(
            f"{weather_data['location']['name']}/"
            f"{weather_data['location']['country']} "
            f"{weather_data['location']['localtime']} "
            f"Weather: {weather_data['current']['temp_c']} Celsius, "
            f"{weather_data['current']['condition']['text']}")
    except requests.RequestException as e:
        print(f"Error fetching weather data: {e}")


if __name__ == "__main__":
    get_weather()
