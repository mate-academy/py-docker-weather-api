import os
import requests


def get_weather() -> None:
    """
    Fetch and print current weather information for Paris.

    Uses Weather API to get current weather data.
    API key is read from API_KEY environment variable.
    """
    api_key = os.environ.get("API_KEY")

    if not api_key:
        print("Error: API_KEY environment variable is not set")
        exit(1)

    base_url = "http://api.weatherapi.com/v1/current.json"
    city = "Paris"

    params = {
        "key": api_key,
        "q": city
    }

    try:
        response = requests.get(base_url, params=params)
        response.raise_for_status()

        data = response.json()

        location = data.get("location", {})
        current = data.get("current", {})
        condition = current.get("condition", {})

        name = location.get("name", "Unknown")
        country = location.get("country", "Unknown")
        temp_c = current.get("temp_c", 0)
        feelslike_c = current.get("feelslike_c", 0)
        condition_text = condition.get("text", "Unknown")
        humidity = current.get("humidity", 0)
        wind_kph = current.get("wind_kph", 0)
        wind_dir = current.get("wind_dir", "N")
        pressure_mb = current.get("pressure_mb", 0)
        localtime = location.get("localtime", "Unknown")

        print(f"Weather in {name}, {country}: ")
        print(f"Temperature: {temp_c}°C")
        print(f"Feels like: {feelslike_c}°C")
        print(f"Condition: {condition_text}")
        print(f"Humidity: {humidity}%")
        print(f"Wind: {wind_kph} kph, {wind_dir}")
        print(f"Pressure: {pressure_mb} mb")
        print(f"Local time: {localtime}")

    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
    except requests.exceptions.ConnectionError:
        print("Error: Cannot connect to Weather API")
    except requests.exceptions.Timeout:
        print("Error: Request timeout")
    except requests.exceptions.RequestException as err:
        print(f"Error fetching weather data: {err}")
    except KeyError as key_err:
        print(f"Error parsing weather data: missing key {key_err}")


if __name__ == "__main__":
    get_weather()
