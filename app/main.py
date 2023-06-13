import os
import requests

from dotenv import load_dotenv


def get_weather() -> None:
    """ Here is a func for getting weather info from Weather API """
    api_key = os.getenv("API_KEY")
    city = os.getenv("CITY")
    base_url = os.getenv("BASE_URL")

    url = f"{base_url}?key={api_key}&q={city}"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        print(
            f"Name: {data['location']['name']}\nLast "
            f"Updated: {data['current']['last_updated']}\n"
            f"Temperature: {data['current']['temp_c']} "
            f"C\nWind Speed: {data['current']['wind_kph']} kph")
    else:
        print(f"Failed to get data, HTTP status code: {response.status_code}")


if __name__ == "__main__":
    load_dotenv()
    get_weather()

