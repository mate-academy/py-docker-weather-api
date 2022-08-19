import requests
import os


URL = "http://api.weatherapi.com/v1/current.json?"
API_KEY = os.environ.get("API_KEY")
PARAMS = {
    "key": API_KEY,
    "q": "Paris"
}


def get_weather():
    request = requests.get(URL, PARAMS)
    city_weather = request.json()

    city = city_weather["location"]["name"]
    country = city_weather["location"]["country"]
    date_ = city_weather["location"]["localtime"]
    temperature = city_weather["current"]["temp_c"]
    condition = city_weather["current"]["condition"]["text"]

    print(f"Weather in {city} \n"
          f"Country: {country} \n"
          f"Date: {date_} \n"
          f"Temperature: {round(temperature)}{chr(176)}C \n"
          f"Condition: {condition}")


if __name__ == "__main__":
    get_weather()
