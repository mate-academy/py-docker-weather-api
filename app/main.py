import os
import requests
from dotenv import load_dotenv

load_dotenv()


def get_weather() -> None:
    api_key = os.environ.get("API_KEY")
    if not api_key:
        print("API_Key is not in environment")
        return
    url = f"http://api.weatherapi.com/v1/current.json?key={api_key}&q=Paris&aqi=no"
    res = requests.get(url)

    if res.status_code != 200:
        print(f"Error: {res.status_code}")
        print(f"Response: {res.text}")
    data = res.json()
    location = data["location"]["name"]
    temperature = data["current"]["temp_c"]
    condition = data["current"]["condition"]["text"]
    humidity = data["current"]["humidity"]
    return f"Weather in {location}: {temperature}C, {humidity}% humidity, condition: {condition}"


if __name__ == "__main__":
    print(get_weather())
