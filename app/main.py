import os

import requests

import io


def get_weather() -> None:
    # write your code here


    CITY = "Paris"
    API_KEY = os.environ.get("API_KEY")
    URL = (f"http://api.weatherapi.com/v1/current.json"
           f"?key={API_KEY}"
           f"&q={CITY}&aqi=no"
           )

    if API_KEY:
        response = requests.get(URL)

        if response.status_code == 200:
            data = response.json()

            country = data.get("location").get("country")
            city = data.get("location").get("name")
            time = data.get("current").get("last_updated")
            temp = str(data.get("current").get("temp_c")) + "°C"
            feel = data.get("current").get("condition").get("text")

            print(f"{city}/{country} {time} Weather: {temp} {feel}")
        else:
            print("Weather API error")
    else:
        print("No API key provided")







if __name__ == "__main__":
    get_weather()
