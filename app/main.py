import os
import requests

BASE_URL = "https://api.weatherapi.com/v1/current.json"
API_KEY = os.getenv("API_KEY")


def get_weather(city: str) -> None:
    if API_KEY is None:
        raise Exception("API_KEY is not set, please set it to proceed")
    params = {"key": API_KEY, "q": city, "aqi": "no"}
    response = requests.get(BASE_URL, params=params)
    if response.status_code != 200:
        raise Exception(f"API request failed "
                        f"{response.status_code}: "
                        f"{response.text}")
    data_response = response.json()
    return print(
        f"Performing request to Weather API for "
        f"city {data_response['location']['name']}...\n"
        f"{data_response['location']['name']}/"
        f"{data_response['location']['country']} "
        f"{data_response['location']['localtime']} "
        f"Weather: {data_response['current']['temp_c']}  "
        f"Celsius, {data_response['current']['condition']['text']}"
    )


if __name__ == "__main__":
    city = input("Enter a city name: ")
    get_weather(city)
