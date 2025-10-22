import requests
import os
from dotenv import load_dotenv

load_dotenv()

URL = "http://api.weatherapi.com/v1/current.json"
API_KEY = os.getenv("API_KEY")
FILTERING = "Paris"
LANG = "en"


def get_weather() -> None:
    url = URL
    api_key = API_KEY
    filtering = FILTERING
    lang = LANG

    result = requests.get(f"{url}?key={api_key}&q={filtering}&lang={lang}")
    data = result.json()

    if "error" in data:
        print("Error:", data["error"]["message"])
        return

    loc = data["location"]
    cur = data["current"]

    city = loc["name"]
    country = loc["country"]
    time = loc["localtime"]
    temp = cur["temp_c"]
    condition = cur["condition"]["text"]

    print(f"{city}/{country} {time} Weather: {temp} Celsius, {condition}")


if __name__ == "__main__":
    get_weather()
