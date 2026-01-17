import os
import requests


def get_weather(city: str = "Paris") -> None:
    api_key = os.environ.get("API_KEY")

    if not api_key:
        print("Error: API_KEY environment variable is not set")
        return

    base_url = "https://api.weatherapi.com/v1/current.json"
    params = {"key": api_key, "q": city, "aqi": "no"}

    try:
        response = requests.get(base_url, params=params)
        response.raise_for_status()

        data = response.json()
        location = data["location"]
        current = data["current"]

        print(f"Weather in {location['name']}, {location['country']}: ")
        print(f"Temperature: {current['temp_c']}°C ({current['temp_f']}°F)")
        print(f"Condition: {current['condition']['text']}")
        print(f"Humidity: {current['humidity']}%")
        print(f"Wind: {current['wind_kph']} km/h")
        print(f"Feels like: {current['feelslike_c']}°C "
              f"({current['feelslike_f']}°F)")

    except requests.exceptions.RequestException as e:
        print(f"Error fetching weather data: {e}")
    except KeyError as e:
        print(f"Error parsing weather data: {e}")


if __name__ == "__main__":
    get_weather()
