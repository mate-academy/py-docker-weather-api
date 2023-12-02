import os
import requests


API_KEY = os.getenv("API_KEY")


def get_weather() -> None:
    response = requests.get(
        "https://api.weatherapi.com/v1/current.json",
        params={
            "key": API_KEY,
            "q": "Paris"
        }
    )

    # Check if the request was successful (status code 2xx)
    if response.status_code == 200:
        weather_data = response.json()
        localtime = weather_data["location"]["localtime"]
        temp_c = weather_data["current"]["temp_c"]
        condition = weather_data["current"]["condition"]["text"]
        print("Performing request to Weather API for city Paris...")
        print(
            f"Paris/France {localtime} "
            f"Weather: {temp_c} Celsius, "
            f"{condition}"
        )
    else:
        print(
            f"Error: Failed to retrieve weather data."
            f" Status Code: {response.status_code}"
        )


if __name__ == "__main__":
    get_weather()
