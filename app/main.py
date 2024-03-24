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

    location = request["location"]
    current_temp = request["current"]
    condition = current_temp["condition"]
    print("▼" * 50)
    print(
        f"{location["name"]}/{location["country"]} {location["localtime"]}\n"
        f"Updated at: {current_temp["last_updated"]} \n"
        f"Weather: {current_temp["temp_c"]} C "
        f"(feels like {current_temp["feelslike_c"]} C), {condition["text"]}"
    )
    print("▲" * 50)

    return request


if __name__ == "__main__":
    city = input("Provide city (or leave empty for Paris): ")

    if city:
        get_weather(city=city)
    else:
        get_weather()
