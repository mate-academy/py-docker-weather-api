import os
import requests


def get_weather() -> None:

    api_key = os.getenv("API_KEY")

    if not api_key:
        raise ValueError("API_KEY environment variable is required")

    url = (
        "http://api.weatherapi.com/v1/current.json"
        f"?key={api_key}&q=Paris"
    )

    response = requests.get(url)
    response.raise_for_status()

    data = response.json()

    city = data["location"]["name"]
    country = data["location"]["country"]
    temp = data["current"]["temp_c"]
    condition = data["current"]["condition"]["text"]

    print(f"City: {city}")
    print(f"Country: {country}")
    print(f"Temperature: {temp}C")
    print(f"Condition: {condition}")


if __name__ == "__main__":
    get_weather()
