import os
import requests


def fetch_weather_data(api_key):
    """Fetch current weather for Paris"""
    url = "http://api.weatherapi.com/v1/current.json"
    params = {
        'key': api_key,
        'q': 'Paris',
        'aqi': 'no'
    }

    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Weather API error: {e}")
        return None


def print_weather(weather_data):
    """Display weather information"""
    if not weather_data:
        print("Failed to get weather data")
        return

    loc = weather_data['location']
    curr = weather_data['current']

    print("\n=== Current Weather in Paris ===")
    print(f"Local time: {loc['localtime']}")
    print(f"Temperature: {curr['temp_c']}°C (Feels like {curr['feelslike_c']}°C)")
    print(f"Conditions: {curr['condition']['text']}")
    print(f"Wind: {curr['wind_kph']} km/h, direction {curr['wind_dir']}")
    print(f"Humidity: {curr['humidity']}%")
    print(f"Pressure: {curr['pressure_mb']} mb\n")


if __name__ == "__main__":
    api_key = os.getenv('WEATHER_API_KEY')
    if not api_key:
        print("Error: WEATHER_API_KEY environment variable required")
        exit(1)

    data = fetch_weather_data(api_key)
    print_weather(data)
