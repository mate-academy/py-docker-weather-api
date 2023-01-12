import os
import requests

def get_weather() -> None:
    base_url = "http://api.weatherapi.com/v1/current.json"
    api_key = os.environ["API_KEY"]
    city = "Paris"

    url = base_url + "?key=" + api_key + "&q=" + city
    response = requests.get(url).json()

    print(
        f"In {response['location']['name']} today current "
        f"temperature in Celsius "
        f"{response['current']['temp_c']}, in Fahrenheit "
        f"{response['current']['temp_f']}. "
        f"Wind speed is {response['current']['wind_mph']} km/hour"
    )


if __name__ == "__main__":
    get_weather()
