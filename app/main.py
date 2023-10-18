import os
import requests


def get_weather() -> None:

    api_key = os.environ.get("API_KEY")
    city = "Paris"
    url = ("https://api.weatherapi.com/v1/current.json?"
           f"key={api_key}&q={city}")

    response = requests.get(url)
    data = response.json()
    city = data["location"]["name"]
    country = data["location"]["country"]
    localtime = data["location"]["localtime"]
    temp_c = data["current"]["temp_c"]
    condition = data["current"]["condition"]["text"]

    if response.status_code == 200:
        print(
            f"{city}/{country} {localtime}"
            f" Weather: {temp_c} Celsius, {condition}"
        )
    else:
        print(f"Error fetching data. Status code: {response.status_code}")


if __name__ == "__main__":
    get_weather()
