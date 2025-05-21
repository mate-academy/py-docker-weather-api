from dotenv import load_dotenv
import requests
import os

load_dotenv()

URL = "https://api.weatherapi.com/v1/current.json"
CITY = "Paris"


def get_weather() -> None:
    api_key = os.getenv("API_KEY")
    if not api_key:
        print("Please, provide your API key!")
        return

    try:
        response = requests.get(f"{URL}?key={api_key}&q={CITY}")
        response.raise_for_status()
        response_json = response.json()

        if "current" in response_json:
            print(f"Celsius: {response_json['current']['temp_c']}")
            print(f"Fahrenheit: {response_json['current']['temp_f']}")
        else:
            print("Unexpected API response structure:", response_json)

    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
    except requests.exceptions.RequestException as req_err:
        print(f"Request error occurred: {req_err}")
    except ValueError:
        print("Error parsing response JSON")


if __name__ == "__main__":
    get_weather()
