import os

import requests


def get_weather(url: str, params: dict):
    res = requests.get(url, params=params)
    response = res.json()

    city = params.get("q")
    current_time_city = response.get("location").get("localtime")
    temperature = response.get("current").get("temp_f")
    last_update_temp = response.get("current").get("last_updated")
    return f"City : {city} \n" \
           f"Current datetime: {current_time_city} \n" \
           f"Temperature: {temperature} C\n" \
           f"Last update temperature datetime: {last_update_temp}"


if __name__ == "__main__":
    params = {
        "q": "Paris",
        "key": os.environ.get("API_KEY")
    }

    url = f"http://api.weatherapi.com/v1/current.json"

    res = get_weather(url, params)
    print(res)
