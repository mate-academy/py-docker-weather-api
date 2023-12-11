import os
import requests
from dotenv import load_dotenv


load_dotenv()


def get_weather(api_key: str, city: str) -> str:
    api_key = os.getenv("API_KEY")
    print(api_key)
    base_url = "http://api.weatherapi.com/v1/current.json"

    try:
        response = requests.get(base_url, params={"key": api_key, "q": city})
        response.raise_for_status()
        weather_data = response.json()

        location = weather_data["location"]["name"]
        country = weather_data["location"]["country"]
        temperature = weather_data["current"]["temp_c"]
        condition = weather_data["current"]["condition"]["text"]

        weather_report = (f"Current weather in {location}, {country}: "
                          f"{temperature}°C, {condition}")
        return weather_report
    except requests.RequestException as e:
        return f"Error fetching weather data: {e}"


if __name__ == "__main__":
    api_key = os.getenv("API_KEY")
    print(get_weather(api_key, "Paris"))
