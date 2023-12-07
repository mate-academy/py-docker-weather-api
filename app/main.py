import os
import json
import requests


URL = "https://api.weatherapi.com/v1/current.json"
FILTERING = "Paris"
API_KEY = os.environ.get("API_KEY")
PARAMS = {
    "q": FILTERING,
    "key": API_KEY,
}


def get_weather() -> None:
    result = requests.get(URL, params=PARAMS)
    json_result = json.loads(result.content)

    print(json_result)

    date = json_result["location"]["localtime"]
    temperature = json_result["current"]["temp_c"]
    condition = json_result["current"]["condition"]["text"]

    print(
        f"Paris/France {date} Weather: {temperature} Celsius, {condition}"
    )


if __name__ == "__main__":
    get_weather()
