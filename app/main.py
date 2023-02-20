import requests
from decouple import config

API_KEY = config("API_KEY")
URL = "https://api.weatherapi.com/v1/current.json?"
FILTERING = "Paris"


def get_weather() -> None:
    url = f"{URL}key={API_KEY}&q={FILTERING}&aqi=yes"
    rq = requests.get(url)
    with open("weather.html", "w") as output_file:
        output_file.write(rq.text)


if __name__ == "__main__":
    get_weather()
