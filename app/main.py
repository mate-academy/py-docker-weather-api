import requests
import os

API_KEY = os.environ.get("API_KEY")

URL = (
    f"http://api.weatherapi.com/v1/current.json"
    f"?key={API_KEY}&aqi=no"
)
FILTERING = "Paris"


def get_weather() -> None:
    print("Performing request to Whether API for city Paris...")

    data = requests.get(URL + f"&q={FILTERING}")
    data = data.json()

    try:
        location = data["location"]
        current_data = data["current"]
        country, city = location["country"], location["name"]
        local_date_and_time = location["localtime"]
        temp_celsius = current_data["temp_c"]
        whether_condition = current_data["condition"]["text"]
    except (KeyError, Exception):
        raise Exception(f"{data}")

    result = (
        f"{city}/{country} {local_date_and_time} "
        f"Wheather: {temp_celsius} Celsius, "
        f"{whether_condition}"
    )

    print(result)


if __name__ == "__main__":
    get_weather()
