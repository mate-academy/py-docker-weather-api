import os
import requests


WEATHER_URL = "http://api.weatherapi.com/v1/current.json?"
API_KEY = os.environ.get("API_KEY")
city = "Paris"
res = requests.get(WEATHER_URL + f"q={city}")


def get_weather() -> None:
    if res.status_code == 200:
        data = res.json()
        main_data = data["main"]

        temperature = main_data["temp_c"]
        wind = main_data["gust_kph"]

        print(f"Current weather in Paris: "
              f"temperature {temperature}, wind {wind}")
    else:
        print("Error occurred :(")


if __name__ == "__main__":
    get_weather()
