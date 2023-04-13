import requests

API_KEY = "c4c72a4109d14453bd0133710231304"
CITY = "Paris"
URL = "http://api.weatherapi.com/v1/current.json"
PAYLOAD = {"key": API_KEY, "q": CITY}


def get_weather() -> None:
    response = requests.get(URL, PAYLOAD).json()

    print(f"{response['location']['name']}"
          f"({response['location']['country']}): "
          f"{response['current']['temp_c']}")


if __name__ == "__main__":
    get_weather()
