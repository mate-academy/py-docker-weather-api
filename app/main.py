import os
import requests
import sys

API_KEY = os.environ.get("API_KEY")
BASE_URL = "http://api.weatherapi.com/v1"


def get_weather() -> None:
    is_automated = not sys.stdin.isatty()

    if not API_KEY:
        print("API_KEY not found in environment variables.")
        return

    while True:
        if is_automated:
            city = os.environ.get("CITY", "Paris")
        else:
            city = input("Enter city name or press Q to exit: ").strip()

            if city.lower() == "q":
                print("Exiting...")
                return

        url = f"{BASE_URL}/current.json?key={API_KEY}&q={city}"

        response = requests.get(url)
        response.raise_for_status()

        data = response.json()

        name = data["location"]["name"]
        country = data["location"]["country"]
        temp_c = data["current"]["temp_c"]
        temp_f = data["current"]["temp_f"]

        print(f"Weather in {name}, {country}: {temp_c}°C ({temp_f}°F)")

        if is_automated:
            return
    #
    # get_weather()


if __name__ == "__main__":
    get_weather()
