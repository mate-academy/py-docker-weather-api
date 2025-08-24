import os
import requests

BASE_URL = "https://api.weatherapi.com/v1/current.json"
CITY = "Paris"
PARAM_KEY = "?key="
PARAM_Q = "&q="


def get_weather() -> None:
    # write your code here
    api_key = os.environ.get("API_KEY")
    if api_key:
        url = BASE_URL + PARAM_KEY + api_key + PARAM_Q + CITY
        print(f"Performing request for Weather API for city {CITY}")
        try:
            response = requests.get(url, timeout=30)
            response.raise_for_status()
            data = response.json()
            location_data = data.get("location")
            current_data = data.get("current")
            city = location_data.get("name")
            if not city:
                city = "Paris"
            country = location_data.get("country")
            if not country:
                country = "France"
            date_time_local = location_data.get("localtime")
            if not date_time_local:
                date_time_local = "time to have a break"
            temp_c = current_data.get("temp_c")
            if temp_c is None:
                temp_c = "N/A"
            condition = current_data.get("condition")
            if "text" in condition:
                condition = condition["text"]
            else:
                condition = "N/A"

            print(f"{city}/{country}"
                  f" {date_time_local} "
                  f"Weather: {temp_c} "
                  f"Celsius, {condition}")
        except requests.exceptions.Timeout:
            print("The request timed out.")
        except requests.exceptions.HTTPError as e:
            if e.response.status_code in (401, 403):
                print("API Key is invalid")
            else:
                print(f"Error: {e}")
        except requests.exceptions.RequestException as e:
            print(f"Error: {e}")

    else:
        print("API Key not set")


if __name__ == "__main__":
    get_weather()
