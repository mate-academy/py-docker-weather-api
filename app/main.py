import os
import requests


def get_weather() -> None:
    """get_weather"""
    key = os.getenv("API_KEY")
    if not key:
        print("API_KEY environment variable not set")
    else:
        url = (f"https://api.weatherapi.com/v1/current.json?key={key} "
               f"&q=Paris&aqi=no")
        weather = requests.get(url)
        if weather.status_code == 200:
            json_file = weather.json()
            print(f"{json_file['location']['name']}/"
                  f"{json_file['location']['country']} "
                  f"{json_file['location']['localtime']} "
                  f"Weather: {json_file['current']['temp_c']} Celsius, "
                  f"{json_file['current']['condition']['text']}")
        else:
            print(f"Error: {weather.status_code}")


if __name__ == "__main__":
    get_weather()
