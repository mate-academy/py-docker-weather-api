import requests
import os

from dotenv import load_dotenv


load_dotenv()


URL = os.getenv("URL", "https://api.weatherapi.com/v1/current.json")
FILTERING = os.getenv("FILTERING", "Kyiv")
API_KEY = os.getenv("API_KEY", None)


def get_weather() -> None:
    if not API_KEY:
        raise ValueError("Env variable is not asigned")

    res = requests.get(URL, params={"q": FILTERING, "key": API_KEY})
    res.raise_for_status()

    res_json = res.json()
    location = res_json["location"]
    weather = res_json["current"]
    print(f"{location['name']}/{location['country']} "
        f"{location['localtime']} Weather: {weather['temp_c']} "
        f"Celsius, {weather['condition']['text']}"
    )


if __name__ == "__main__":
    get_weather()
