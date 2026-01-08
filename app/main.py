import os
import requests


API_KEY = os.getenv("API_KEY")
CITY = "Paris"
URL = "http://api.weatherapi.com/v1/current.json"


def get_weather_data(city: str, api_key: str) -> dict:
    params = {"key": api_key, "q": city, "aqi": "no"}
    response = requests.get(URL, params=params)
    response.raise_for_status()
    return response.json()


def print_weather(weather_data: dict) -> None:
    location = weather_data["location"]
    current = weather_data["current"]

    print(
        f"Weather in {location['name']}, {location['country']}: \n"
        f"Temperature: {current['temp_c']}°C\n"
        f"Condition: {current['condition']['text']}\n"
        f"Wind: {current['wind_kph']} km/h\n"
        f"Humidity: {current['humidity']}%"
    )


def get_weather() -> None:
    if not API_KEY:
        print("ERROR: API_KEY not set!")
        return

    try:
        data = get_weather_data(CITY, API_KEY)
        print_weather(data)
    except requests.exceptions.HTTPError as e:
        print(f"HTTP Error: {e}")
        print("Check if your API_KEY is correct")
    except requests.exceptions.ConnectionError:
        print("Connection Error: Cannot connect to Weather API")
    except KeyError as e:
        print(f"Error parsing weather data: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")


if __name__ == "__main__":
    get_weather()
