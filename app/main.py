import os
import requests


def get_weather() -> None:
    api_key = os.getenv("API_KEY")
    city = "Paris"
    url = f"http://api.weatherapi.com/v1/current.json?key={api_key}&q={city}"

    response = requests.get(url)
    data = response.json()

    print(
        f"{data['location']['name']}/{data['location']['country']} "
        f"{data['current']['last_updated']} Weather: "
        f"{data['current']['temp_c']} Celsius, "
        f"{data['current']['condition']['text']}"
    )


if __name__ == "__main__":
    get_weather()
