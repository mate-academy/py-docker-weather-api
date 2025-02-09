import os
import requests

API_KEY = os.getenv("API_KEY")

if not API_KEY:
    raise ValueError("API_KEY environment variable is not set. Please set it.")

CITY = "Paris"
URL = \
    f"http://api.weatherapi.com/v1/current.json?key={API_KEY}&q={CITY}&aqi=no"


def get_weather() -> str:
    response = requests.get(URL)
    if response.status_code == 200:
        try:
            data = response.json()
            if (
                    "current" in data
                    and "temp_c" in data["current"]
                    and "condition" in data["current"]
                    and "text" in data["current"]["condition"]
            ):

                print(f"Weather in {CITY}: {data['current']['temp_c']}°C, "
                      f"{data['current']['condition']['text']}")
            else:
                print("Error: Expected keys are missing in the API response.")
        except ValueError:
            print("Error: Unable to parse the JSON response.")
    else:
        print(
            f"Error:{response.status_code}."
        )


if __name__ == "__main__":
    get_weather()
