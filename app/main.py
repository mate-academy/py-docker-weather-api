import os
import requests

URL = "https://api.weatherapi.com/v1/current.json?"
FILTERING = "Paris"
KEY = os.environ.get("API_KEY")


def get_weather() -> None:
    weather_dict = requests.get(
        URL,
        params={"q": FILTERING, "key": KEY}
    ).json()

    location = (f"{weather_dict['location']['name']}"
                f"/{weather_dict['location']['country']}")
    local_time = weather_dict["location"]["localtime"]
    temperature = weather_dict["current"]["temp_c"]
    condition_text = weather_dict["current"]["condition"]["text"]

    info = (
        f"{location} {local_time} "
        f"Weather: {temperature} Celsius, {condition_text}"
    )

    print(info)


if __name__ == "__main__":
    get_weather()
