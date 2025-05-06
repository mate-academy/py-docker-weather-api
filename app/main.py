import os
import requests

API_KEY = os.environ.get("API_KEY")
URL = "http://api.weatherapi.com/v1/current.json"
PARAMS = {
    "key": API_KEY,
    "q": "Paris",
    "aqi": "no"
}


def get_weather() -> None:
    if not API_KEY:
        print("❌ API_KEY is missing. "
              "Please set it as an environment variable.")
        return

    try:
        response = requests.get(URL, params=PARAMS, timeout=5)
        response.raise_for_status()
        data = response.json()

        city = data["location"]["name"]
        country = data["location"]["country"]
        time = data["location"]["localtime"]
        temperature = data["current"]["temp_c"]
        condition = data["current"]["condition"]["text"]

        print(f"{city}/{country} {time} "
              f"Weather: {temperature}°C, {condition}")

    except requests.exceptions.HTTPError as http_err:
        try:
            error_data = response.json()
            message = error_data.get("error", {}).get("message", str(http_err))
        except Exception:
            message = str(http_err)
        print(f"❌ HTTP error: {message}")

    except requests.exceptions.RequestException as req_err:
        print(f"❌ Network error: {req_err}")

    except KeyError as key_err:
        print(f"❌ Missing expected data: {key_err}")
