import requests
import os


def get_weather() -> None:
    res = requests.get(
        "http://api.weatherapi.com/v1/current.json",
        params={
            "key": os.environ.get("API_KEY"),
            "q": "paris"
        }
    )

    print(
        f"{res.json()['location']['name']}/"
        f"{res.json()['location']['country']} "
        f"{res.json()['location']['localtime']} "
        f"Weather: {res.json()['current']['temp_c']} Celsius, "
        f"{res.json()['current']['condition']['text']}"
    )


if __name__ == "__main__":
    get_weather()
