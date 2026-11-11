import os

import requests

API_URL = "https://api.weatherapi.com/v1/current.json"
CITY = "Paris"


def get_weather(city: str) -> None:
    api_key = os.getenv("API_KEY")

    if not api_key:
        raise ValueError("API_KEY is not set")

    print(f"Performing weather API request for city {city}...")

    try:
        response = requests.get(
            API_URL,
            params={
                "key": api_key,
                "q": city,
            },
            timeout=10,
        )
        response.raise_for_status()

    except requests.RequestException as e:
        print(f"Error occurred: {e}")
        return

    res_data = response.json()

    cleaned_res = (
        f"{res_data['location']['name']}/"
        f"{res_data['location']['country']} "
        f"{res_data['location']['localtime']} "
        f"Weather: {res_data['current']['temp_c']} Celsius, "
        f"{res_data['current']['condition']['text']}"
    )

    print(cleaned_res)


if __name__ == "__main__":
    get_weather(CITY)
