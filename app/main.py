import os
import requests


def get_weather() -> None:
    city = "Paris"
    api_key = os.getenv("API_KEY")

    response = requests.get(
        f"https://api.weatherapi.com/v1/current.json?key={api_key}&q={city}"
    )

    if response.ok:
        data = response.json()
        country = data["location"]["country"]
        current = data["current"]
        date = current["last_updated"]
        temperature = current["temp_c"]
        condition = current["condition"]["text"]
        print(
            f"{city}/{country} {date} "
            f"Weather: {temperature} Celsius, {condition}"
        )

    else:
        print("Failed to retrieve weather information.")


if __name__ == "__main__":
    get_weather()
