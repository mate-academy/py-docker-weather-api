import os
import requests


def get_weather():
    API_KEY = os.environ["API_KEY"]
    data = requests.get(f"http://api.weatherapi.com/v1/current.json?key={API_KEY}&q=Paris").json()

    print("Paris: "
          f"datetime: {data['location']['localtime']} "
          f"Temperature: {data['current']['temp_c']} C°, "
          f"{data['current']['condition']['text']}")


if __name__ == "__main__":
    get_weather()
