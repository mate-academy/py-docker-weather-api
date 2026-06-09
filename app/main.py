import os
import requests

URL = "http://api.weatherapi.com/v1/current.json"
CITY = "Paris"


def get_weather(api_key: str) -> None:
    url = f"{URL}?key={api_key}&q={CITY}"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        temp = data["current"]["temp_c"]
        text = data["current"]["condition"]["text"]
        print(f"Weather in {CITY}: {temp} Celsius, {text}")
    else:
        print(f"Error: {response.status_code}")


def main() -> None:
    api_key = os.getenv("API_KEY")
    if not api_key:
        print("API_KEY is not set!")
        return
    get_weather(api_key)


if __name__ == "__main__":
    main()
