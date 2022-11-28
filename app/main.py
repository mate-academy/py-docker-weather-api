import os

import requests
import json

API_KEY = os.environ.get("API_KEY")
URL = "https://api.weatherapi.com/v1/current.json"
FILTERING = "Paris"


def get_weather() -> None:

    params = {"key": API_KEY, "q": FILTERING}
    result = requests.get(URL, params=params)

    received_data = json.loads(result.content)

    print(
        f"""
        {received_data['location']['name']}
        ({received_data['location']['localtime']})
        Temperature: {received_data['current']['temp_c']} °C
        Condition: {received_data['current']['condition']['text']}
        """
    )


if __name__ == "__main__":
    get_weather()
