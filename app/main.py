import requests
from decouple import config

URL = "https://api.weatherapi.com/v1/current.json?"
API_KEY = config("API_KEY", default="some-key", cast=str)
CITY = "Paris"


def get_weather() -> None:
    """
    Returns string representation of weather in Paris in following format:
    {city}/{country} {date time} Weather: {temperature} Celsius, {text}
    """

    print(f"Performing request to Weather API to city {CITY}")

    result_json = requests.get(URL, params={"key": API_KEY, "q": CITY}).json()

    city = result_json["location"]["name"]
    country = result_json["location"]["country"]
    localtime = result_json["location"]["localtime"]
    temp_celsius = result_json["current"]["temp_c"]
    condition = result_json["current"]["condition"]["text"]

    print(
        f"{city}/{country} {localtime} "
        f"Weather: {temp_celsius} Celsius, {condition}"
    )


if __name__ == "__main__":
    get_weather()
