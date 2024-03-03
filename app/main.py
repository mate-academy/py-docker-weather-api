import requests


def get_weather() -> None:
    # write your code here
    url = ("http://api.weatherapi.com/v1/current."
           "json?key=8326749241e34abdb6095927240303&q=Paris")

    response = requests.get(url)
    data = response.json()

    return data


if __name__ == "__main__":
    get_weather()
