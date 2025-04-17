from dotenv import load_dotenv
import os
import requests

load_dotenv()
BASE_URL = "http://api.weatherapi.com/v1"


def get_weather(city: str, ) -> None:
    api_key = os.getenv("API_KEY")
    url = f"{BASE_URL}/current.json?key={api_key}&q={city}"
    response = requests.get(url)

    if response.status_code == 200:
        api_wer = response.json()
        city_name = api_wer["location"]["name"]
        country_name = api_wer["location"]["country"]
        local_time = api_wer["location"]["localtime"]
        temp_c = api_wer["current"]["temp_c"]
        condition = api_wer["current"]["condition"]["text"]
        print(
            f"{city_name}/{country_name}"
            f" {local_time} Weather: "
            f"{temp_c} Celsius, {condition}"
        )
    else:
        print("Error fetching the weather data.")


if __name__ == "__main__":
    get_weather("Paris")
