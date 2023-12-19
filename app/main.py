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

    city_name = weather_data.get("location", {}).get("name", "Unknown city")
    country = weather_data.get("location", {}).get("country", "Unknown country")
    local_time = weather_data.get("location", {}).get("localtime", "Unknown time")
    temp_c = weather_data.get("current", {}).get("temp_c", "N/A")
    condition_text = weather_data.get("current", {}).get("condition", {}).get("text", "N/A")

    formatted_output = (
        f"{city_name}/{country}"
        f" {local_time} Weather: {temp_c} "
        f"Celsius, {condition_text}"
    )
    print(formatted_output)


if __name__ == "__main__":
    get_weather()
