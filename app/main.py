import requests
import os


def get_weather() -> None:

    api_key = os.environ.get("API_KEY")

    url = (f"http://api.weatherapi.com/v1/current."
           f"json?key={api_key}&q=Paris")

    response = requests.get(url)

    data = response.json()

    print(f"Performing request to "
          f"Weather API for city {data['location']['name']}...")

    print(f"{data['location']['name']}/{data['location']['country']}"
          f" {data['location']['localtime']} "
          f"Weather: {data['current']['temp_c']}"
          f" Celsius, {data['current']['condition']['text']}"
          )


if __name__ == "__main__":
    get_weather()
