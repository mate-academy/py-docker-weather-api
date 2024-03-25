import os
import requests
from dotenv import load_dotenv

load_dotenv()

URL = "http://api.weatherapi.com/v1/current.json"
API_KEY = os.getenv("API_KEY")
CITY = "Paris"
LANGUAGE = "en"


def get_weather() -> None:
    res = requests.get(
        URL,
        params={
            "key": API_KEY,
            "q": CITY,
            "units": "metric",
            "lang": LANGUAGE
        }
    )
    data = res.json()

    if "error" in data:
        print("Error:", data["error"]["message"])
    else:
        location = data["location"]
        weather = data["current"]

        print("Country:", location["country"])
        print("City:", location["name"])
        print("Localtime:", weather["last_updated"])
        print("Condition:", weather["condition"]["text"])
        print(
            "Temperature C:", weather["temp_c"],
            ", feels like", weather["feelslike_c"]
        )
        print(
            "Temperature F:", weather["temp_f"],
            ", feels like", weather["feelslike_f"]
        )

        humidity = weather["humidity"]
        wind_speed = weather["wind_kph"]
        pressure = weather["pressure_mb"]

        print("Humidity:", humidity, "%")
        print("Wind Speed:", wind_speed, "kph")
        print("Pressure:", pressure, "mb")


if __name__ == "__main__":
    get_weather()
