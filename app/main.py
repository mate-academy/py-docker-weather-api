import requests
import os


def get_weather() -> None:
    url = "https://api.weatherapi.com/v1/current.json"
    filtering = "Paris"

    api_key = os.getenv("API_KEY")
    if not api_key:
        raise Exception("API_KEY environment variable not set")

    print("Performing request to Weather API for city Paris...")
    response = requests.get(
        url,
        params={
            "key": api_key,
            "q": filtering,
        }
    )
    if response.status_code != 200:
        raise Exception("Weather API request failed")

    needed_data = response.json().get("current")
    print(
        f"Weather: {needed_data.get('temp_c', None)} Celsius, "
        f"{needed_data.get('condition', None).get('text', None)}."
    )


if __name__ == "__main__":
    get_weather()
