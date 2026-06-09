import os
import sys
import requests

URL = "http://api.weatherapi.com/v1/current.json"
CITY = "Paris"


def main() -> None:
    api_key = os.environ.get("API_KEY")

    if not api_key:
        print(
            "Error: API_KEY environment variable is not set.", file=sys.stderr
        )
        sys.exit(1)

    params = {"key": api_key, "q": CITY, "aqi": "no"}

    try:
        response = requests.get(URL, params=params)
        response.raise_for_status()
        data = response.json()

        location = data["location"]["name"]
        country = data["location"]["country"]
        local_time = data["location"]["localtime"]
        temp_c = data["current"]["temp_c"]
        condition = data["current"]["condition"]["text"]

        print(f"Performing request to Weather API for city {CITY}...")
        print(
            f"{location}/{country} {local_time} "
            f"Weather: {temp_c} Celsius, {condition}"
        )

    except requests.exceptions.RequestException as e:
        print(f"Error fetching data from Weather API: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
