import os

import requests
from dotenv import load_dotenv


def get_weather() -> None:
    load_dotenv()
    api_key = os.getenv("API_KEY")

    url = (f"https://api.weatherapi.com/v1/current.json?key="
           f"{api_key}&q=Paris&aqi=no")

    try:
        response = requests.get(url)
        response.raise_for_status()
        weather_data = response.json()

        if "current" in weather_data:
            current_weather = weather_data["current"]
            temperature = current_weather["temp_c"]
            description = current_weather["condition"]["text"]

            print(f"Weather in Paris: {temperature}°C, {description}.")
        else:
            print(f"Error: {weather_data.get('error', 
                            {}).get('message', 'Unknown error')}")

    except requests.exceptions.RequestException as e:
        print(f"Request error: {e}")


if __name__ == "__main__":
    get_weather()
