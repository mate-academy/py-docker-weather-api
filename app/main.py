import os
import requests

API_KEY = os.getenv('API_KEY')
FILTER = 'Paris'
BASE_URL = 'http://api.weatherapi.com/v1/current.json'

def get_weather() -> None:

    if not API_KEY:
        print('API key not found!')
    else:
        result = requests.get(BASE_URL + f"?key={API_KEY}&" + f"q={FILTER}")

        if result.status_code == 200:
            data = result.json()
            city = data["location"]["name"]
            country = data["location"]["country"]
            day_time = data["location"]["localtime"]
            temperatura = data["current"]["temp_c"]
            type_weather = data["current"]["condition"]["text"]
            print(f"{city}/{country} {day_time} "
                  f"Weather: {temperatura} {type_weather}")
        else:
            print("Error: invalid request")


if __name__ == "__main__":
    get_weather()
