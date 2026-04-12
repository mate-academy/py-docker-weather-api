import os

import requests


def get_weather() -> None:
    # write your code here
    url_city = "Paris"
    url_api_key = os.environ.get("API_KEY")
    url = (f"http://api.weatherapi.com/v1/current.json"
           f"?key={url_api_key}"
           f"&q={url_city}&aqi=no"
           )

    if url_api_key:
        response = requests.get(url)

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
