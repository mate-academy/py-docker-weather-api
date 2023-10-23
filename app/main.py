import requests
import os


URL = "https://api.weatherapi.com/v1/current.json?"
CITY = "Paris"
FILTERING = f"&q={CITY}"
KEY = "key=" + os.environ.get("API_KEY")


def get_weather() -> None | str:
    res = requests.get(URL + KEY + FILTERING)

    if res.status_code != 200:
        return print("Something goes wrong:(")

    json_data = res.json()

    time = json_data["location"]["localtime"]
    condition = json_data["current"]["condition"]["text"]
    temperature = json_data["current"]["temp_c"]
    temperature_feels_like = json_data["current"]["feelslike_c"]
    wind = json_data["current"]["wind_kph"]
    wind_direction = json_data["current"]["wind_dir"]
    humidity = json_data["current"]["humidity"]

    forecast = (
        f"Forecast in Paris at {time}:\n"
        f"The weather is: {condition}\n"
        f"Temperature: {temperature} °C\n"
        f"Feels Like: {temperature_feels_like} °C\n"
        f"Wind: {wind} km/h\n"
        f"Wind Direction: {wind_direction}\n"
        f"Humidity: {humidity}%"
    )

    print(forecast)


if __name__ == "__main__":
    get_weather()
