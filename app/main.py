import requests
import os


API_KEY = os.getenv("API_KEY")
CITY = "Paris"

if not API_KEY:
    raise ValueError("API_KEY not found. Please, provide it.")

def get_weather() -> None:
    url = f"http://api.weatherapi.com/v1/current.json?key={API_KEY}&q={CITY}"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        location = data["location"]["name"]
        country = data["location"]["country"]
        temp_c = data["current"]["temp_c"]
        condition = data["current"]["condition"]["text"]

        print(f"📍 Weather in {location}, {country}")
        print(f"🌡️ Temperature: {temp_c}°C")
        print(f"⛅ Condition: {condition}")

    else:
        print("Failed to fetch weather data.")
        print("Status code:", response.status_code)
        print("Response:", response.text)


if __name__ == "__main__":
    get_weather()
