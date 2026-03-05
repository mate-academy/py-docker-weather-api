import requests
from dotenv import load_dotenv
import os


load_dotenv()

API_KEY = os.getenv("API_KEY")

URL = "https://api.weatherapi.com/v1/current.json"
FILTERING = "Paris"


def get_weather() -> None:
    result = requests.get(URL, params={"key": API_KEY, "q": FILTERING})
    data = result.json()
    print("Performing request to Weather API for city Paris...")
    print(
        f"{data['location']['name']}/"
        f"{data['location']['country']}"
        f" {data['location']['localtime']}"
        f" Weather {data['current']['temp_c']} "
        f"Celsius"
    )


if __name__ == "__main__":
    get_weather()
