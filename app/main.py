import os
import requests


def get_weather(
        url: str = "http://api.weatherapi.com/v1/current.json",
        city: str = "Paris"
) -> None:
    print(f"Performing request to Weather API for city {city}...")

    key = os.environ["API_KEY"]

    request_url = f"{url}?key={key}&q={city}"
    try:
        response = requests.get(request_url).json()

        message = (
            f"{response['location']['name']}/{response['location']['country']}"
            f" {response['location']['localtime']} Weather: "
            f"{response['current']['temp_c']} Celsius, "
            f"{response['current']['condition']['text']}"
        )

        print(message)
    except requests.exceptions.RequestException as e:
        print(f"HTTP request failed: {e}")


if __name__ == "__main__":
    get_weather()
