import os
import requests
from requests import Response


API_KEY = os.environ.get("API_KEY")
URL = "http://api.weatherapi.com/v1/current.json?"


def get_weather(city: str = "Paris") -> Response:
    print(f"Requesting {city} weather from Weather API...")
    request = requests.get(
        URL + f"key={API_KEY}&q={city}&aqi=no"
    ).json()

    if "error" in request:
        print(request["error"]["message"])
        return request

    city_name = request["location"]["name"]
    country = request["location"]["country"]
    localtime = request["location"]["localtime"]
    current_temp = request["current"]["temp_c"]
    updated_at = request["current"]["last_updated"]
    feels_like = request["current"]["feelslike_c"]
    condition = request["current"]["condition"]["text"]

    print("▼" * 50)
    print(
        f"{city_name}/{country} {localtime}\n"
        f"Updated at: {updated_at} \n"
        f"Weather: {current_temp} C (feels like {feels_like} C), {condition}"
    )
    print("▲" * 50)

    return request


if __name__ == "__main__":
    city = input("Provide city (or leave empty for Paris): ")

    if city:
        get_weather(city=city)
    else:
        get_weather()
