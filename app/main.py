def get_weather() -> None:
    URL = "http://api.weatherapi.com/?"
    FILTERING = "Paris"

    result = requests.get(URL + f"q={FILTERING}")


if __name__ == "__main__":
    get_weather()
