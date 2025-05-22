import os
import requests

from dotenv import load_dotenv


load_dotenv()


URL = "http://api.weatherapi.com/v1/current.json?"

CITY = "Paris"


def get_weather() -> None:
    api_key = os.environ.get("WEATHER_API_KEY")
    if not api_key:
        raise ValueError("WEATHER_API_KEY is not set in environment variables")
    try:
        result = requests.get(
                URL + f"key={api_key}" + f"&q={CITY}"
            )

        if result.status_code == 200:
            print(result.json())
        else:
            print(f"Error: Received status code {result.status_code}")
            if result.status_code == 404:
                print("Resource not found")
            elif result.status_code == 500:
                print("Server error")
            else:
                print(f"Unexpected status code: {result.status_code}")

    except requests.exceptions.ConnectionError:
        print("Error: Failed to connect to the server. Please check your network connection.")

    except requests.exceptions.Timeout:
        print("Error: The request timed out.")
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
    except requests.exceptions.RequestException as e:
        print(f"Error during request: {e}")
    except ValueError as ve:
        print(f"Error: Unable to parse JSON response - {ve}")

if __name__ == "__main__":
    get_weather()
