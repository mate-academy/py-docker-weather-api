import os
import requests

from requests import Response


API_KEY = os.environ.get("API_KEY")
URL = "http://api.weatherapi.com/v1/current.json?"


def get_weather(city: str = "Paris") -> Response:
    print(f"Requesting {city} weather from Weather API...")

    params = {"key": API_KEY, "q": city, "aqi": "no"}
    request = requests.get(URL, params=params)
    request_json = request.json()

    if request.status_code != 200:
        error = request_json.get("error")
        if error:
            print(error.get("message"))
        return request

    city_name = request_json["location"]["name"]
    country = request_json["location"]["country"]
    localtime = request_json["location"]["localtime"]
    current_temp = request_json["current"]["temp_c"]
    updated_at = request_json["current"]["last_updated"]
    feels_like = request_json["current"]["feelslike_c"]
    condition = request_json["current"]["condition"]["text"]

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
