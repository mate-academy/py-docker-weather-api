import requests
import os


def get_weather() -> None:
    URL = "https://api.weatherapi.com/v1/current.json"
    API_KEY = os.environ.get("API_KEY")
    CITY = "Paris"
    response = requests.get(URL, params={"key": API_KEY, "q": CITY})
    response_json = response.json()

    print(
        f"{response_json['location']['name']}/"
        f"{response_json['location']['country']} "
        f"{response_json['location']['localtime']} "
        f"Weather: {response_json['current']['temp_c']} Celsius, "
        f"{response_json['current']['condition']['text']}"
    )


if __name__ == "__main__":
    get_weather()
