import os
import requests
from dotenv import load_dotenv

load_dotenv()
FILTERING = "Paris"
API_KEY = os.getenv("API_KEY")
URL = "https://api.weatherapi.com/v1/current.json"


def get_weather() -> None:
    params = {"key": API_KEY, "q": FILTERING}
    res = requests.get(URL, params=params).json()
    if res.get("error") is not None:
        print(res.get("error"))
        return
    print(
        f"Country: {res.get('location').get('country')};\n"
        f"City: {res.get('location').get('name')};\n"
        f"Time: {res.get('location').get('localtime')};\n"
        f"Weather: {res.get('current').get('condition').get('text')}\n"
        f"Temperature: {res.get('current').get('temp_c')} Celsius;"
    )


if __name__ == "__main__":
    get_weather()
