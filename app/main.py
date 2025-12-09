import os

import requests
print(os.environ.get("API_KEY"))

API_KEY=os.environ.get("API_KEY")
CITY = "Paris"

def get_weather() -> None:

    url = f"http://api.weatherapi.com/v1/current.json"
    params = {
        "key": API_KEY,
        "q": CITY,
    }
    response = requests.get(url, params=params)
    print(response.json())



if __name__ == "__main__":
    get_weather()
