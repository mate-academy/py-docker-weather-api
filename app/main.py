import os
import httpx
from dotenv import load_dotenv

load_dotenv()

BASE_URL = "http://api.weatherapi.com/v1/current.json"
API_KEY = os.getenv("API_KEY")


def get_weather(query: str = "Paris") -> None:
    params = {
        "q": query,
        "key": API_KEY,
    }
    with httpx.Client() as client:
        res = client.get(BASE_URL, params=params)
    data = res.json()
    location = data["location"].get("name", "Unknown")
    region = data["location"].get("region", "Unknown")
    country = data["location"].get("country", "Unknown")
    time = data["current"].get("last_updated", "Unknown")
    temperature = data["current"].get("temp_c", "Unknown")
    condition = data["current"]["condition"].get("text", "Unknown")
    print(
        f"{location} - {country} - {region} - {time}\n"
        f"Now is {condition} - {temperature} degrees"
    )


if __name__ == "__main__":
    get_weather()
