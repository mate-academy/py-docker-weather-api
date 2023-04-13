import requests

CITY = "Paris"
URL = "http://api.weatherapi.com/v1/current.json"
API_KEY = "3e243be0a1204288bfc132613231304"


def get_weather() -> None:

    response = requests.get(URL, params={"key": {API_KEY}, "q": {CITY}})

    if response.status_code == 200:
        data = response.json()

        print(f"Location: {data['location']['name']},"
              f" {data['location']['country']}"
              f" (local date/time: {data['location']['localtime']})\n"
              f"Temperature: {data['current']['temp_c']} Celsius"
              f" / {data['current']['temp_f']} Fahrenheit"
              f" |-> {data['current']['condition']['text']}\n"
              f"Wind speed: {data['current']['wind_kph']}"
              f" kilometers per hours")

    print("Recheck url and params in 'get' method")


if __name__ == "__main__":
    get_weather()
