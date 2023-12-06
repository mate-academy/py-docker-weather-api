import requests
import os

API_KEY = os.environ.get("API_KEY")
CITY = "Paris"

URL = "http://api.weatherapi.com/v1/current.json"


def get_weather() -> None:
    params = {
        "key": API_KEY,
        "q": CITY
    }

    print("Performing request to Weather API for city Paris...")
    response = requests.get(URL, params=params)

    if response.status_code != 200:
        print(f"Error occurred, response status code: {response.status_code}")
        return None

    data = response.json()
    return data


if __name__ == "__main__":
    data = get_weather()

    print(
        f"{data['location']['name']}/{data['location']['country']} "
        f"{data['location']['localtime']} "
        f"Weather: {data['current']['temp_c']} Celsius, "
        f"{data['current']['condition']['text']}"
    )

