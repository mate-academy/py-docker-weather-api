import os

import requests

KPH_TO_MPS_CONSTANT = 0.277777778
URL = "https://api.weatherapi.com/v1/current.json"
API_KEY = os.environ.get("API_KEY")
CITY = "Paris"


def get_weather() -> None:
    response = requests.get(url=URL, params={"key": API_KEY, "q": CITY})
    data = {
        "country": response.json().get("location").get("country"),
        "city": response.json().get("location").get("name"),
        "temperature (°C)": response.json().get("current").get("temp_c"),
        "wind (m/s)": round(
            response.json().get("current").get("wind_kph")
            * KPH_TO_MPS_CONSTANT,
            1,
        ),
        "humidity (%)": response.json().get("current").get("humidity"),
        "cloud (%)": response.json().get("current").get("cloud"),
    }
    print(data)


if __name__ == "__main__":
    get_weather()
