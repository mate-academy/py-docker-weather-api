import requests

from decouple import config


API_KEY = config("API_KEY")
URL = "https://api.weatherapi.com/v1/current.json"
CITY = "Paris"
PARAMS = {
    "key": API_KEY,
    "q": CITY,
}


def get_weather() -> None:
    response = requests.get(url=URL, params=PARAMS)

    if response.status_code == 200:
        data = response.json()

        city = data.get("location")["name"]
        region = data.get("location")["region"]
        country = data.get("location")["country"]
        localtime = data.get("location")["localtime"]
        temperature = data.get("current")["temp_c"]
        condition = data.get("current")["condition"]["text"]

        print(
            f"{city}/{region}/{country}, date/time: {localtime} \n"
            f"Weather: {temperature} Celsius, {condition}"
        )

    else:
        print(response.status_code)


if __name__ == "__main__":
    get_weather()
