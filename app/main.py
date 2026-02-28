import requests
import os


def get_weather() -> None:

    weather_api_key = os.environ.get("API_KEY")
    base_url = "http://api.weatherapi.com/v1/current.json"
    city = "Paris"

    if not weather_api_key:
        print("Error: API_KEY is not set.")
        return

    url = f"{base_url}?key={weather_api_key}&q={city}"

    response = requests.get(url)
    response.raise_for_status()

    data = response.json()
    city = data["location"]["name"]
    country = data["location"]["country"]
    localtime = data["location"]["localtime"]
    temp = data["current"]["temp_c"]
    condition = data["current"]["condition"]["text"]

    print(
        f"{city}/{country} {localtime} Weather: {temp} Celsius, {condition}"
    )


if __name__ == "__main__":
    get_weather()
