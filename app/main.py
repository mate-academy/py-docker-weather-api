import requests
import os

URL = "https://api.weatherapi.com/v1/current.json"
CITY = "London"
KEY = os.getenv("KEY")


def get_weather() -> None:
    try:
        response = requests.get(
            URL,
            params={
                "key": KEY,
                "q": CITY
            }
        )
        data = response.json()

        country = data["location"]["country"]
        city = data["location"]["name"]
        cur_weather = data["current"]["temp_c"]
        date = data["location"]["localtime"]

        print(f"***{date}***\n"
              f"***{country}***\n"
              f"Weather in the city: {city}\n"
              f"Temperature: {cur_weather}")

    except Exception:
        print("Information not correct!")


if __name__ == "__main__":
    get_weather()
