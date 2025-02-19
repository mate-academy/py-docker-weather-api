import os
import requests
import logging


def get_weather() -> None:
    api_key = os.environ.get("WEATHER_API_KEY")
    if not api_key:
        logging.error("Error: API key was not found in environ variables!")
        return

    city = "Paris"
    base_url = "https://api.weatherapi.com/v1/current.json"
    url = f"{base_url}?key={api_key}&q={city}"

    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        logging.error(f"Request error: {e}")
        return

    try:
        weather_data = response.json()
        current_weather = weather_data.get("current", {})
        if current_weather:
            temperature = current_weather.get("temp_c", "N/A")
            condition = current_weather.get("condition", {}).get("text", "N/A")
            logging.error(
                f"The weather in {city}: {temperature}°C, {condition}"
            )
        else:
            logging.error("Can not get weather data.")
    except ValueError:
        logging.error("JSON parsing error. The response is not valid JSON.")


if __name__ == "__main__":
    get_weather()
