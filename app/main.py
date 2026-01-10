import os
import requests

CITY = "Paris"
URL = "https://api.weatherapi.com/v1/current.json"


def get_weather() -> None:
    try:
        api_key = os.getenv("api_key")
        if not api_key:
            print("Error: api_key environment variable is not set")
            return

        params = {
            "key": api_key,
            "q": CITY,
            "lang": "en",
        }

        response = requests.get(URL, params=params, timeout=10)
        response.raise_for_status()

        data = response.json()

        print(
            f"{data['location']['name']}/{data['location']['country']} "
            f"{data['location']['localtime']} "
            f"Weather: {data['current']['temp_c']} Celsius, "
            f"{data['current']['condition']['text']}"
        )

    except requests.exceptions.RequestException as e:
        print(f"Network/API error: {e}")
    except ValueError:
        print("Error: Failed to parse JSON response from API.")
    except KeyError as e:
        print(f"Error: Missing expected data in API response: {e}")


if __name__ == "__main__":
    get_weather()
