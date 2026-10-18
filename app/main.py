import requests
import os

API_KEY = os.getenv("API_KEY")
CITY = "Paris"
URL = "http://api.weatherapi.com/v1/current.json"

if not API_KEY:
    print("Not found!")


def get_weather() -> None:
    params = {
        "key": API_KEY,
        "q": CITY,
        "aqi": "no"
    }
    try:

        response = requests.get(URL, params)
        response.raise_for_status()
        response_in_json = response.json()

        location = response_in_json["location"]
        country = location["country"]
        city = location["name"]
        request_time = location["localtime"]
        current = response_in_json["current"]
        temp_in_celsius = current["temp_c"]
        condition = current["condition"]
        text = condition["text"]
        wind_speed = current["wind_kph"]

        print(f"Country: {country}\n"
              f"City: {city}\n"
              f"Time: {request_time}\n"
              f"{text}\n"
              f"Temperature in Celsius: {temp_in_celsius}\n"
              f"Wind speed: {wind_speed}\n")
    except requests.exceptions.HTTPError as err:
        print(f"HTTP Error: {err}")
    except requests.exceptions.RequestException as err:
        print(f"Connection problem: {err}")


if __name__ == "__main__":
    if API_KEY:
        get_weather()
