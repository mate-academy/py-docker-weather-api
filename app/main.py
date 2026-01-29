import os
import requests


def get_weather(city_name: str) -> None:
    api_key = os.environ.get("API_KEY")
    if not api_key:
        raise ValueError("API_KEY environment variable not set!")

    URL = f"http://api.weatherapi.com/v1/current.json?"
    FILTERING = f"key={api_key}&q={city_name}&aqi=no"
    response = requests.get(URL + FILTERING)
    data = response.json()

    country = data["location"]["country"]
    localtime = data["location"]["localtime"]
    temp_c = data["current"]["temp_c"]
    temp_condition = data["current"]["condition"]["text"]

    print(f"Performing request to Weather API for city {city_name}...")
    print(f"{city_name}/{country} {localtime} Weather: {temp_c} Celsius, {temp_condition}")


if __name__ == "__main__":
    city = os.environ.get("CITY", "Paris")
    get_weather(city)
