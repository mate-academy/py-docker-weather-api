import requests
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("API_KEY")
URL = "http://api.weatherapi.com/v1/"
FILTERING = "Paris"


def get_weather(url, filtering, api_key) -> None:

    endpoint = f"current.json?key={api_key}&q={filtering}"
    request_url = url + endpoint
    response = requests.get(request_url)

    if response.status_code == 200:
        weather_data = response.json()
        print(f"[+] Weather received successfully\n"
              f"Location: {weather_data['location']['country']}/{weather_data['location']['name']}\n"
              f"Today is {weather_data['current']['condition']['text']}\n"
              f"{weather_data['current']['temp_c']} degrees Celsius")
    else:
        print(f"[-] Error: {response.status_code}")


if __name__ == "__main__":
    get_weather(URL, FILTERING, API_KEY)
