import requests


def get_weather() -> requests.Response:

    URL = "https://www.weatherapi.com/weather/q/"
    FILTERING = "paris-ile-de-france-france-803267"

    paris_weather = requests.get(URL + f"q={FILTERING}")
    return paris_weather


if __name__ == "__main__":
    get_weather()
