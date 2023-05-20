import requests
import os

URL = "http://api.weatherapi.com/v1/current.json?"
API_KEY = os.getenv("API_KEY")
CITY = "Paris"


def get_weather() -> None:
    response = requests.get(URL, params={"key": API_KEY, "q": CITY})
    if response.status_code == 200:
        response = response.json()
        print(f"Performing request for Weather Api for city {CITY}...")
        print(
            f"Location: {response['location']['name']}/"
            f"{response['location']['country']}"
            f" {response['location']['localtime']}"
            f" Weather: {response['current']['temp_c']}"
            f" Celsius, {response['current']['condition']['text']}"
        )
    else:
        print("Please, check your API_KEY or availability of Weather site")


if __name__ == "__main__":
    get_weather()
