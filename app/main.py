import os
import requests


BASE_URL = "https://api.weatherapi.com/v1/current.json"
CITY = "Paris"


def get_weather() -> None:
    api_key = os.getenv("API_KEY")

    if not api_key:
        raise ValueError("API_KEY is not provided")
    url = f"{BASE_URL}?key={api_key}&q={CITY}"
    response = requests.get(url)
    data = response.json()
    if "error" in data:
        print("Error:", data["error"]["message"])
        return
    temp = data["current"]["temp_c"]
    condition = data["current"]["condition"]["text"]
    print(f"Paris/France Weather: {temp} {condition}")


if __name__ == "__main__":
    get_weather()
