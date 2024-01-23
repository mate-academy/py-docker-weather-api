import os
import requests


API_KEY = os.environ.get("API_KEY")
BASE_URL = "http://api.weatherapi.com/v1"
FILTERING = "Paris"


def get_weather() -> None:
    weather_endpoint = f"{BASE_URL}/current.json?key={API_KEY}&q={FILTERING}"
    weather_response = requests.get(weather_endpoint)
    timezone_endpoint = f"{BASE_URL}/timezone.json?key={API_KEY}&q={FILTERING}"
    timezone_response = requests.get(timezone_endpoint)

    if (
        weather_response.status_code == 200
        and timezone_response.status_code == 200
    ):
        current_weather = weather_response.json()
        time_zone_weather = timezone_response.json()

        condition_text = current_weather["current"]["condition"]["text"]
        country = time_zone_weather["location"]["country"]
        date_and_time = time_zone_weather["location"]["localtime"]
        temperature_in_celsius = current_weather["current"]["temp_c"]

        print(
            f"Weather API request for city {FILTERING}/{country} "
            f"{date_and_time} "
            f"Weather: {temperature_in_celsius} Celsius, "
            f"{condition_text}"
        )

    else:
        print(
            f"Failed to retrieve weather data. Status code: "
            f"{weather_response.status_code} for weather response. "
            f"Status code: "
            f"{timezone_response.status_code} for timezone response."
        )


if __name__ == "__main__":
    get_weather()
