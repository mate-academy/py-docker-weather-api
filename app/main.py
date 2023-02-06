import os

import requests

import dotenv


def get_weather() -> None:
    url = "https://api.weatherapi.com/v1/current.json"

    dotenv.load_dotenv()
    # get method of requests module
    # return response object
    response = requests.get(url, params={
        "key": os.getenv("API_KEY"),
        "q": "Paris"
    })

    # json method of response object
    # convert json format data into
    # python format data
    weather_list = response.json()

    # Now weather_list contains list of nested dictionaries
    current = weather_list.get("current")
    city = f"City: {weather_list.get('location').get('name')}"
    temp_c = f"Temperature C : {current.get('temp_c')}"
    temp_f = f"Temperature F: {current.get('temp_f')}"
    condition = f"Condition : {current.get('condition').get('text')}"
    wind = f"Wind : {current.get('wind_mph')}"

    print(f"""The weather
    {city}
    {temp_c}
    {temp_f}
    {condition}
    {wind}""")


if __name__ == "__main__":
    get_weather()
