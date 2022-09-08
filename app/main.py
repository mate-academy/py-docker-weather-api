import os
import requests


def get_weather():

    key = os.getenv("API_KEY")
    data = requests.get(
        f"http://api.weatherapi.com/v1/current.json?key={key}&q=Paris"
    ).json()

    print(
        f"Paris, {data['location']['localtime']} "
        f"Temperature: {data['current']['temp_c']} C°, "
    )


if __name__ == "__main__":
    get_weather()
