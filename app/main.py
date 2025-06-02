import json
import requests


def get_weather() -> None:
    url = "https://api.weatherapi.com/v1/current.json?key=d1fe3b5d476a4b0494d155040250206&q=Paris"
    res = requests.get(url)
    data = res.json()

    its_necessary_data = {
        "Country": data["location"]["country"],
        "Time&Date": data["location"]["localtime"],
        "Temperature": data["current"]["temp_c"],
    }
    with open("weather.json", "w", encoding="utf-8") as f:
        json.dump(its_necessary_data, f, ensure_ascii=False, indent=2)


if __name__ == "__main__":
    get_weather()
