import requests


def get_weather() -> None:
    weather_in_paris_current = requests.get("http://api.weatherapi.com/v1/current.json?"
                                    "key=8b89884a56104151964200013222711&q=Paris")
    print(weather_in_paris_current.text)


if __name__ == "__main__":
    get_weather()
