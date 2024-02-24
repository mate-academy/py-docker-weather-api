import os
import requests


def get_weather() -> None:
    city = "Paris"
    api_url = (
        f"http://api.weatherapi.com/v1/current.json?key={api_key}&q={city}"
    )

    try:
        response = requests.get(api_url)
        data = response.json()
        print(
            f"Weather in {city}: {data['current']['condition']['text']}"
            f"Temperature: {data['current']['temp_c']}°C"
        )
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    api_key = os.environ.get("API_KEY")
    get_weather()
