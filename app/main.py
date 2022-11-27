import requests
import os


def get_weather() -> None:
    api_key = os.environ["API_KEY"]
    print(f"Running with API key: {api_key}, weather in Paris now (JSON):")
    weather_in_paris_current = requests.get(
        "http://api.weatherapi.com/v1/current.json?"
        f"key={api_key}&q=Paris"
    )
    print(weather_in_paris_current.text)


if __name__ == "__main__":
    get_weather()
