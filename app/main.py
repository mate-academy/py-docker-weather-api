import requests
import os

API_KEY = os.environ.get("API_KEY")
CITY = "Paris"


def get_weather() -> None:
    if not API_KEY:
        raise ValueError("API_KEY environment variable not set")

    url = f"http://api.weatherapi.com/v1/current.json?q={CITY}&key={API_KEY}"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        print(data)
        print(f"City: {data['location']['name']}")
        print(f"Temperature: {data['current']['temp_c']}°C")
        print(f"Condition: {data['current']['condition']['text']}")
        print(f"Wind speed in kilometres: {data['current']['wind_kph']}")
        print(f"Humidity: {data['current']['humidity']}")
    else:
        print(f"Error: {response.status_code} - {response.text}")


if __name__ == "__main__":
    get_weather()
