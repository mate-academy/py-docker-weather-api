import os
import requests

API_URL = "https://api.weatherapi.com/v1/current.json"
API_KEY = os.environ.get("API_KEY")


def get_weather() -> None:
    if not API_KEY:
        print("API_KEY environment variable is not set.")
        return

    response = requests.get(API_URL, params={"key": API_KEY, "q": "Paris"})

    if response.status_code != 200:
        print(f"Failed to retrieve weather data. Status code: "
              f"{response.status_code}")
        return

    response_data = response.json()

    if "error" in response_data:
        print(f"Error from Weather API: {response_data['error']['message']}")
        return

    location_info = response_data.get("location", {})
    if location_info:
        weather_info = response_data.get("current", {})
        if weather_info:
            print(f"{location_info['name']}/{location_info['country']} "
                  f"{location_info['localtime']} "
                  f"Weather: {weather_info.get('temp_c')} "
                  f"Celsius, "
                  f"{weather_info.get('condition', {}).get('text', '')}")
        else:
            print("Weather information not found in the response.")
    else:
        print("Location information not found in the response.")


if __name__ == "__main__":
    get_weather()
