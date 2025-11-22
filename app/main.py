import os
import requests

def get_weather() -> None:
    api_key = os.getenv("API_KEY")
    if not api_key:
        raise Exception("API_KEY environment variable is not set")
    url = "http://api.weatherapi.com/v1/current.json"
    params = {
        "key": api_key,
        "q": "Paris",
        "days": 14,
    }
    res = requests.get(url, params=params)
    data = res.json()
    print(f"{data['location']['name']}/{data['location']['country']} {data['location']['localtime']} Weather: {data['current']['temp_f']} {data['current']['condition']['text']}")


if __name__ == "__main__":
    get_weather()
