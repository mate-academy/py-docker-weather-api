import os
import requests

URL = "http://api.weatherapi.com/v1/current.json"
FILTERING = "Paris"


def get_weather() -> None:
    api_key = os.environ.get("API_KEY")

    if not api_key:
        raise EnvironmentError("API_KEY environment variable is not set")

    params = {
        "key": api_key,
        "q": FILTERING
    }

    result = requests.get(URL, params=params)

    if result.status_code == 200:
        data = result.json()
        print("Performing request to Weather API for city Paris...")
        print(
            f"{data['location']['name']}/{data['location']['country']}"
            f" {data['location']['localtime']}"
            f" Weather: {data['current']['temp_c']} Celsius, "
            f"{data['current']['condition']['text']}"
        )
    else:
        print(f"Error {result.status_code}: {result.text}")


if __name__ == "__main__":
    get_weather()
