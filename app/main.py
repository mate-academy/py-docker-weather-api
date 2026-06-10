import os
import requests


def get_weather() -> None:
    api_key = os.environ.get("API_KEY")

    if not api_key:
        raise EnvironmentError("API_KEY environment variable is not set.")

    city = "Paris"
    url = f"""
    http://api.weatherapi.com/v1/current.json?key={api_key}&q={city}&aqi=no
    """

    response = requests.get(url)
    response.raise_for_status()
    data = response.json()

    location = data["location"]
    current = data["current"]

    print(f"Performing request to Weather API for city {city}")

    name = location["name"]
    country = location["country"]
    localtime = location["localtime"]
    date, time = localtime.split(" ")
    hour_minute = time[:5]
    temp = current["temp_c"]
    condition = current["condition"]["text"]

    print(
        f"{name}/{country} {date} {hour_minute} \
Weather: {temp} Celsius, {condition}"
    )


if __name__ == "__main__":
    get_weather()
