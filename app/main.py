import requests

API_KEY = "3647e2845af24914ad1111124231304"
FILTERING = "Paris"
URL = "https://api.weatherapi.com/v1/current.json"


def get_weather() -> None:

    params = {
        "key": API_KEY,
        "q": FILTERING
    }

    response = requests.get(URL, params=params)
    info = response.json()

    city = info.get("location").get("name")
    temperature = info.get("current").get("feelslike_c")
    wind = info.get("current").get("wind_mph")

    print(
        f"In {city} weather for today: \n"
        f"    Temperature | {temperature} C*; \n"
        f"    Wind        | {wind} m/h;"
    )


if __name__ == "__main__":
    get_weather()
