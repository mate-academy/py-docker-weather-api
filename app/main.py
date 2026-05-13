import os
import requests


def get_weather() -> None:
    api_key = os.environ.get("API_KEY")

    if not api_key:
        print("API key not set")
        return

    city = "Paris"
    url = (f"http://api.weatherapi.com/v1/current.json?key="  # noqa: E231
           f"{api_key}&q={city}")

    request = requests.get(url)
    data = request.json()

    country = data["location"]["country"]
    current_time = data["location"]["localtime"]
    celsius = data["current"]["temp_c"]
    weather_description = data["current"]["condition"]["text"]

    print(
        f"{city}/{country} {current_time} "
        f"Weather: {celsius} Celsius, {weather_description}"
    )


if __name__ == "__main__":
    get_weather()
