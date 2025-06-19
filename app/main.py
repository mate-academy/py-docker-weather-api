import os
import requests
from dotenv import load_dotenv

load_dotenv()


api_key = os.environ.get("API_KEY")
URL = "http://api.weatherapi.com/v1/current.json"
CITY = "Paris"


def get_weather() -> None:
    if not api_key:
        raise EnvironmentError("API key not found.")
    response = requests.get(
        f"{URL}?key={api_key}&q={CITY}"
    )

    if response.status_code == 200:
        data = response.json()
        print(
            f"{data['location']['name']}/{data['location']['country']}  {data['location']['localtime']}  Weather: {data['current']['temp_c']} Celsius, {data['current']['condition']['text']}"
        )
    else:
        print(response.status_code)


if __name__ == "__main__":
    get_weather()
