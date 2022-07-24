import ast
import os

import requests


def get_weather():
    base_url = "http://api.weatherapi.com/v1"
    json = ".json?"
    key = "API_KEY"
    option = "/current"
    api_key = os.environ.get(key)
    city = "Paris"
    response = requests.get(f"{base_url}{option}{json}key={api_key}&q={city}")
    dict_str = response.content.decode("UTF-8")
    my_data = ast.literal_eval(dict_str)
    print(
        "Performing request to Weather API for city Paris...\n"
        f"{my_data['location']['name']}/{my_data['location']['country']} "
        f"{my_data['location']['localtime']} "
        f"Weather: {my_data['current']['temp_c']} Celsius, "
        f"{my_data['current']['condition']['text']}"
    )


if __name__ == "__main__":
    get_weather()
