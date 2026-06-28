import os
import requests


def get_weather() -> None:
    api_key = os.environ.get("API_KEY")
    url = "http://api.weatherapi.com/v1/current.json"
    request = requests.get(
        url,
        {"key": api_key, "q": "Paris"}
    )
    data = request.json()
    city = data["location"]["name"]
    country = data["location"]["country"]
    time = data["location"]["localtime"]
    temp = data["current"]["temp_c"]
    text = data["current"]["condition"]["text"]
    print(f"{city}/{country} {time} Weather: {temp} Celsius, {text}")


if __name__ == "__main__":
    get_weather()
