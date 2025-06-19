import os
import requests


def get_weather() -> None:
    api_key = os.environ.get("API_KEY")
    if not api_key:
        print("Error: API_KEY environment variable not set.")
        return

    city = "Paris"
    url = f"http://api.weatherapi.com/v1/current.json?key={api_key}&q={city}&aqi=no"

    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()

        location = data.get("location", {})
        current = data.get("current", {})

        name = location.get("name", "Unknown city")
        country = location.get("country", "")
        time = location.get("localtime", "")
        temp = current.get("temp_c", "N/A")
        condition = current.get("condition", {}).get("text", "Unknown")

        print(f"{name}/{country} {time} Weather: {temp}° Celsius, {condition}")

    except requests.RequestException as e:
        print(f"Request failed: {e}")
    except ValueError:
        print("Error parsing response JSON.")


if __name__ == "__main__":
    get_weather()
