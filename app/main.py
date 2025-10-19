import os
import requests

if os.path.exists(".env"):
    try:
        import dotenv
    except ImportError:
        print("python-dotenv not installed; skipping .env loading")
    else:
        dotenv.load_dotenv()


URL = "https://api.weatherapi.com/v1/current.json?"
FILTERING = "Paris"
API_KEY = os.getenv("API_KEY")

if not API_KEY:
    raise ValueError(
        "API_KEY not found! Ensure you have set up "
        "your API key throw Docker or in .env file."
    )


def get_weather() -> None:

    result = requests.get(URL + f"key={API_KEY}&q={FILTERING}")
    result.raise_for_status()
    data = result.json()

    location = data.get("location")
    if not location:
        raise ValueError("Missing 'location' field in API response")

    city = location.get("name")
    country = location.get("country")

    current = data.get("current")
    if not current:
        raise ValueError("Missing 'current' field in API response")

    temperature = current.get("temp_c")
    last_update = current.get("last_updated")

    condition = current.get("condition")
    if not condition:
        raise ValueError("Missing 'condition' field in API response")

    weather_condition = condition.get("text")

    print(
        f"Performing request to Weather API for city {city}...\n"
        f"{city}/{country} {last_update} Weather: {temperature} Celsius, "
        f"{weather_condition}"
    )


if __name__ == "__main__":
    get_weather()
