import os
import requests
from prettytable import PrettyTable


URL = "https://api.weatherapi.com/v1/current.json?"
FILTERING = "Paris"


def get_weather() -> None:
    payload = {
        "q": FILTERING,
        "key": os.environ["API_KEY"]
    }

    result = requests.get(URL, params=payload).json()
    location = result["location"]
    current = result["current"]

    pretty = PrettyTable(
        ["LOCATION", f"{location['name']}/{location['country']}"]
    )
    pretty.add_rows(
        [
            ["Temperature", f"{current['temp_c']}°C | {current['temp_f']}°F"],
            [
                "Feels like",
                f"{current['feelslike_c']}°C | {current['feelslike_f']}°F"
            ],
            ["Condition", current["condition"]["text"]],
            [
                "Wind speed",
                f"{current['wind_mph']} mph | {current['wind_kph']} kph"
            ],
            ["Humidity", f"{current['humidity']}%"]
        ]
    )

    print(f"Weather forcast for {location['localtime']}")
    print(pretty)


if __name__ == "__main__":
    get_weather()
