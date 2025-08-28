import requests
import os


BASE_URL = "http://api.weatherapi.com/v1/current.json?"
CITY = "Paris"


def get_weather() -> None:
    api_key = os.getenv("API_KEY")
    if not api_key:
        print("Error: API_KEY is not set.")
        return
    else:
        try:
            result = requests.get(
                BASE_URL + f"key={api_key}&" + f"q={CITY}",
                timeout=5
            )
            result.raise_for_status()
        except requests.RequestException as error:
            print(f"Network error: {error}")
            return
        data = result.json()
        city = data["location"]["name"]
        country = data["location"]["country"]
        day_time = data["location"]["localtime"]
        temperatura = data["current"]["temp_c"]
        type_weather = data["current"]["condition"]["text"]
        print(f"{city}/{country} {day_time} "
              f"Weather: {temperatura} {type_weather}")


if __name__ == "__main__":
    get_weather()
