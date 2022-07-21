import os

import requests


def get_weather():
    key = os.environ["API_KEY"]
    url = f"https://api.weatherapi.com/v1/current.json?key={key}&q=Paris&aqi=yes"
    result = requests.get(url)
    pars_data = result.json()
    print(f"Performing request to Weather API for city {pars_data['location']['name']}...\n"
          f"{pars_data['location']['name']}/"
          f"{pars_data['location']['country']} "
          f"{pars_data['location']['localtime']} "
          f"Weather: {pars_data['current']['temp_c']} Celsius, "
          f"{pars_data['current']['condition']['text']}"
          )


if __name__ == "__main__":
    get_weather()
