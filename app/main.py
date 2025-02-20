import os
import requests


def get_weather() -> None:
    url = "https://api.weatherapi.com/v1/current.json?"
    filtering = "London"

    api_key = os.getenv("API_KEY")
    if not api_key:
        raise ValueError("The API_KEY must be set!")

    response = requests.get(url + f"key={api_key}&q={filtering}")
    data = response.json()

    city = data["location"]["name"]
    country = data["location"]["country"]
    local_time = data["location"]["localtime"]
    temp = data["current"]["temp_c"]
    weather = data["current"]["condition"]["text"]

    print(f"{city}/{country} {local_time} Weather: {temp} Celsius, {weather}")


if __name__ == "__main__":
    get_weather()
