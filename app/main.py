import requests
import os


def get_weather() -> None:
    weather_data = requests.get("https://api.weatherapi.com/v1/current.json"
                                f"?key={os.environ.get('API_KEY')}&q=paris")
    weather_dict = weather_data.json()
    print(f"{weather_dict['location']['name']}/"
          f"{weather_dict['location']['country']} "
          f"{weather_dict['location']['localtime']} Weather: "
          f"{weather_dict['current']['temp_c']} Celsius, "
          f"{weather_dict['current']['condition']['text']}")


if __name__ == "__main__":
    get_weather()
