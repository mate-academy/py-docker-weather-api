import os
import requests


BASE_URL = "https://api.weatherapi.com/v1/current.json"


def get_weather() -> None:
    api_key = os.getenv("API_KEY")
    city = os.getenv("CITY", "Paris")

    if not api_key:
        print("Error: API_KEY environment variable is not set")
        return

    params = {
        "key": api_key,
        "q": city,
        "aqi": "no",
    }

    try:
        response = requests.get(BASE_URL, params=params, timeout=10)
        data = response.json()

        if response.status_code != 200:
            error_message = (
                data.get("error", {})
                .get("message", "Unknown error")
            )
            print(f"Error: {error_message}")
            return

        city_name = data["location"]["name"]
        country = data["location"]["country"]
        local_time = data["location"]["localtime"]
        temperature = data["current"]["temp_c"]
        condition = data["current"]["condition"]["text"]

        print(
            f"{city_name}/{country} {local_time} "
            f"Weather: {temperature} Celsius, {condition}"
        )

    except requests.exceptions.RequestException as error:
        print(f"Connection error: {error}")


if __name__ == "__main__":
    get_weather()
