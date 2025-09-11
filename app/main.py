import os
import sys
from typing import Any

import requests
from dotenv import load_dotenv

load_dotenv()


def get_weather() -> dict[str, Any]:
    api_key = os.getenv("API_KEY")
    if not api_key:
        print(
            "❌ Error: API_KEY was not found in the changes.",
            file=sys.stderr
        )
        sys.exit(1)
    city = "Paris"
    url = "http://api.weatherapi.com/v1/current.json"
    params = {"key": api_key, "q": city}
    response = requests.get(url, params=params)
    response.raise_for_status()
    data = response.json()
    return data


if __name__ == "__main__":
    result = get_weather()
    print("Full weather in Paris: ", result)
