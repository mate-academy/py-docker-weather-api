import os
import requests


BASE_URL = "http://api.weatherapi.com/v1/current.json"


def get_weather(city: str = "Paris") -> None:
    api_key = os.getenv("API_KEY")
    if not api_key:
        raise ValueError("API_KEY environment variable is not set")

    url = f"{BASE_URL}?key={api_key}&q={city}"

    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        data = response.json()

        location = data["location"]["name"]
        country = data["location"]["country"]
        temp_c = data["current"]["temp_c"]
        condition = data["current"]["condition"]["text"]
        localtime = data["location"]["localtime"]

        print(
            f"{location}/{country} {localtime} "
            f"Weather: {temp_c} Celsius, {condition}"
        )
    except requests.RequestException as e:
        print(f"Request failed: {e}")
    except KeyError as e:
        print(f"Unexpected response format. Missing key: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    get_weather()
