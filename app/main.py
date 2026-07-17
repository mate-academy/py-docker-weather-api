import os
import requests


def get_weather() -> None:
    api_key = os.getenv("API_KEY")
    if not api_key:
        raise ValueError("API_KEY environment variable is not set")

    url = "https://api.weatherapi.com/v1/current.json"
    params = {
        "key": api_key,
        "q": "Paris",
    }
    response = requests.get(url, params=params)
    response.raise_for_status()
    data = response.json()
    print(f"City: {data['location']['name']}")
    print(f"Country: {data['location']['country']}")
    print(f"Temperature: {data['current']['temp_c']}°C")
    print(f"Condition: {data['current']['condition']['text']}")


if __name__ == "__main__":
    get_weather()
