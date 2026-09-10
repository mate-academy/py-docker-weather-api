import os
import requests


def get_weather() -> None:
    print("Performing request to Weather API for city Paris...")

    api_key = os.getenv("API_KEY")
    if not api_key:
        raise ValueError("API_KEY environment variable not set")

    city = "Paris"
    params = {
        "key": api_key,
        "q": city
    }

    response = requests.get(
        "https://api.weatherapi.com/v1/current.json",
        params=params,
    )

    data = response.json()

    print(
        f"{data['location']['name']}/{data['location']['country']} "
        f"{data['location']['localtime']} "
        f"Weather: {data['current']['temp_c']} Celsius, "
        f"{data['current']['condition']['text']}"
    )


if __name__ == "__main__":
    get_weather()
