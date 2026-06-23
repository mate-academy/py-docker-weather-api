import os
import requests


def get_weather() -> None:
    api_key = os.environ["API_KEY"]
    city = "Paris"

    url = (
        f"http://api.weatherapi.com/v1/current.json"
        f"?key={api_key}&q={city}"
    )

    response = requests.get(url)
    data = response.json()

    location = data["location"]
    current = data["current"]

    city_name = location["name"]
    country = location["country"]
    localtime = location["localtime"]
    temp = current["temp_c"]
    condition = current["condition"]["text"]

    date, time = localtime.split(" ")

    print(f"{city_name}/{country} "
          f"{date} {time}"
          f" Weather: {temp} Celsius, {condition}")


if __name__ == "__main__":
    get_weather()
