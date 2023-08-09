import os
import requests


url = "http://api.weatherapi.com/v1/current.json"
api = os.environ.get("API_KEY")
city = "Paris"


def get_weather() -> None:
    params = {"q": city, "key": api}

    response = requests.get(url, params=params)
    res = response.json()

    country = res.get("location").get("country")
    current = res.get("current")
    current_time = current.get("last_updated")
    temp = current.get("temp_c")
    feelslike = current.get("feelslike_c")
    condition = current.get("condition").get("text")
    wind = current.get("wind_kph")

    print(f"{city}/{country} {current_time} \n"
          f"Weather: \n"
          f"    Temperature: {temp}°C, feels like {feelslike}°C \n"
          f"    Condition: {condition}\n"
          f"    Wind: {wind} km/h")


if __name__ == "__main__":
    get_weather()
