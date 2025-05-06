import os
import requests


def get_weather() -> None:
    api_key = os.getenv("API_KEY")

    if not api_key:
        print(
            "API_KEY is not set."
            " Make sure to provide it via environment variable."
        )
        exit(1)

    city = "Paris"

    url = f"http://api.weatherapi.com/v1/current.json?key={api_key}&q={city}"

    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        weather = data["current"]["condition"]["text"]
        temperature = data["current"]["temp_c"]

        print(f"Weather in {city}: {weather}")
        print(f"Temperature: {temperature}°C")
    else:
        print(f"Error: {response.status_code}")


if __name__ == "__main__":
    get_weather()
