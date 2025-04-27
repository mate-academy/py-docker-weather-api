import os
import requests
from dotenv import load_dotenv


load_dotenv()


API_KEY = os.getenv("API_KEY")


# function works not only for Paris city!!!
def get_weather() -> None:
    if not API_KEY:
        print("API_KEY is not set. Make sure the environment variable is set.")
        exit(1)

    city = input("Enter the city name: ")

    url = f"http://api.weatherapi.com/v1/current.json?key={API_KEY}&q={city}"

    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        weather = data["current"]["condition"]["text"]
        temperature = data["current"]["temp_c"]

        print(f"Weather in {city}: {weather}")
        print(f"Temperature: {temperature}°C")
    else:
        print(f"Error: {response.status_code}")


if __name__ == "__main__":
    get_weather()
