import os
import requests


def get_weather() -> None:

    api_key = os.getenv("API_KEY")
    city = "Paris"

    if not api_key:
        raise ValueError("API_KEY environment variable is missing")

    url = f"http://api.weatherapi.com/v1/current.json?key={api_key}&q={city}"

    response = requests.get(url)
    data = response.json()

    city = data['location']['name']
    country = data['location']['country']
    localtime = data['location']['localtime']
    temp = data['current']['temp_c']
    condition = data['current']['condition']['text']

    print(f"{city}/{country} {localtime} Weather: {temp} Celsius, {condition}")


if __name__ == "__main__":
    get_weather()
