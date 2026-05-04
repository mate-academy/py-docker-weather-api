import requests
import os
from dotenv import load_dotenv

load_dotenv()

wheather_api_key = os.environ.get("WHEATHER_API_KEY")


def get_weather() -> None:
    print("Performing request to Whether API for city Paris...")

    url = (
        f"http://api.weatherapi.com/v1/current.json"
        f"?key={wheather_api_key}&q=Paris&aqi=no"
    )

    data = requests.get(url)
    data = data.json()

    try:
        location = data["location"]
        current_data = data["current"]
        country, city = location["country"], location["name"]
        local_date_and_time = location["localtime"]
        temp_celsius = current_data["temp_c"]
        whether_condition = current_data["condition"]["text"]
    except KeyError or Exception:
        raise Exception(f"{data}")

    result = (
        f"{country}/{city} {local_date_and_time} "
        f"Whether: {temp_celsius} Celsius, "
        f"{whether_condition}"
    )

    print(result)


if __name__ == "__main__":
    get_weather()
