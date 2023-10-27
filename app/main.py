import os
import requests
import dotenv

dotenv.load_dotenv()

FILTERING = "Paris"

API_KEY = os.getenv("API_KEY")

URL = "https://api.weatherapi.com/v1/current.json"


def get_weather() -> None:
    params = {"key": API_KEY, "q": FILTERING}
    res = requests.get(URL, params=params).json()
    error = res.get("error", None)
    if error is not None:
        print(error)
        return
    location = res.get("location", {})
    current = res.get("current", {})

    print(
        f"Country: {location.get('country', 'N/A')};\n"
        f"City: {location.get('name', 'N/A')};\n"
        f"Time: {location.get('localtime', 'N/A')};\n"
        f"Weather: {current.get('condition', {}).get('text', 'N/A')}\n"
        f"Temperature: {current.get('temp_c', 'N/A')} Celsius;"
    )


if __name__ == "__main__":
    get_weather()
