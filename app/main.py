import os

import requests


def get_weather() -> None:
    # write your code here
    api_key = os.getenv("API_KEY")
    response = requests.get(
        (
            f"https://api.weatherapi.com/v1/"
            f"current.json?q=Paris&"
            f"key={api_key}"
        )
    )

    if response.status_code == 200:
        weather_data = response.json()

        location = weather_data.get("location", {}).get("name")
        temperature = weather_data.get("current", {}).get("temp_c")
        condition = weather_data.get("current", {}).get("condition", {}).get("text")

        print(
            f"The current weather in {location} is:\n"
            f"Temperature: {temperature} degrees Celsius\n"
            f"Weather condition: {condition}"
        )
    elif response.status_code == 403:
        print("Please enter API_KEY. Current API_KEY is not valid.")
    else:
        print("Error occurred while fetching weather data")


if __name__ == "__main__":
    get_weather()
