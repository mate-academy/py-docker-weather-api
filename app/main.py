import os
import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("API_KEY")
URL = "http://api.weatherapi.com/v1/current.json"
CITY = "Kiev"


def get_weather() -> None:
    params = {
        "key": API_KEY,
        "q": CITY
    }

    response = requests.get(url=URL, params=params)

    if response.status_code == 200:
        weather_dict = response.json()
        region = weather_dict["location"]["region"]
        country = weather_dict["location"]["country"]
        date, time = weather_dict["current"]["last_updated"].split(" ")
        temperature = weather_dict["current"]["temp_c"]
        description = weather_dict["current"]["condition"]["text"]
        mess_to_user = (
            f"Your region: {region}\n"
            f"Country: {country}\n"
            f"City: {CITY}\n"
            f"Date: {date}\n"
            f"Time: {time}\n"
            f"Temperature (degrees): {temperature}\n"
            f"Weather: {description}\n"
        )
        print(mess_to_user)
    else:
        print("Error! Wrong 'API KEY' or no such city exists!Tray again!")


if __name__ == "__main__":
    get_weather()
