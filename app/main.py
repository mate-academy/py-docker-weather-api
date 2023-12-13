import requests
import os

API_KEY = os.environ.get("API_KEY")
URL = "http://api.weatherapi.com/v1/current.json"
CITY = "Paris"


def get_weather() -> None:
    params = {"key": API_KEY, "q": CITY}
    print("Performing request to Weather API for city Paris...")
    response = requests.get(URL, params=params)
    if response.status_code == 200:
        print(
            f"{response.json()['location']['name']}/"
            f"{response.json()['location']['country']} "
            f"{response.json()['location']['localtime']} "
            f"Weather: {response.json()['current']['temp_c']} Celsius, "
            f"{response.json()['current']['condition']['text']}"
        )
    else:
        print(f"Error occurred, response status code: {response.status_code}")


if __name__ == "__main__":
    get_weather()
