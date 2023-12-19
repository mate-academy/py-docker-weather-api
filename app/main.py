import os
import requests


BASE_URL = "https://api.weatherapi.com/v1/current.json"
CITY = "Paris"


def get_weather() -> None:
    api_key = os.getenv("API_KEY")
    if not api_key:
        raise ValueError("No API_KEY set for Weather API")
    print("Performing request to Weather API for city Paris..")

    params = {
        "key": api_key,
        "q": CITY,
    }

    response = requests.get(BASE_URL, params=params)
    weather_data = response.json()

    city_name = weather_data["location"]["name"]
    country = weather_data["location"]["country"]
    local_time = weather_data["location"]["localtime"]
    temp_c = weather_data["current"]["temp_c"]
    condition_text = weather_data["current"]["condition"]["text"]

    formatted_output = (
        f"{city_name}/{country}"
        f" {local_time} Weather: {temp_c} "
        f"Celsius, {condition_text}"
    )
    print(formatted_output)


if __name__ == "__main__":
    get_weather()
