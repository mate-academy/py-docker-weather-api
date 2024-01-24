import os
import requests


def get_weather() -> None:
    base_url = "https://api.weatherapi.com/v1/current.json?"
    api_key = os.getenv("API_KEY")

    city = "Paris"

    url = base_url + "key=" + api_key + "&q=" + city

    response = requests.get(url).json()
    result = (
        f"{city}/{response['location']['country']} "
        f"{response['location']['localtime']} "
        f"Weather: {response['current']['temp_c']} Celsius, "
        f"{response['current']['condition']['text']}"
    )

    print(result)


if __name__ == "__main__":
    get_weather()
