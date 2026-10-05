import os
import requests


API_KEY = os.environ.get("API_KEY")
CITY = "Paris"
URL = "http://api.weatherapi.com/v1/current.json"


def get_weather() -> None:

    try:
        response = requests.get(
            URL,
            params={
                "key": API_KEY,
                "q": CITY,
            }
        )
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f"Error occurred: {e}")
        raise

    data = response.json()
    condition = data["current"]["condition"]["text"]
    temperature = data["current"]["temp_c"]
    print(
        f"Weather in {CITY}: "
        f"{condition}, "
        f"{temperature} Celsius"
    )


if __name__ == "__main__":
    get_weather()
