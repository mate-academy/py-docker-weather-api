import requests
import os


URL = "http://api.weatherapi.com/v1/current.json?"
FILTERING = "Kyiv"


def get_weather() -> str:

    res = requests.get(f"{URL}key={os.environ.get("API_KEY")}&q={FILTERING}")

    if res.status_code == 200:
        data = res.json()
        location = data["location"]["name"]
        temperature = data["current"]["temp_c"]

        print(f"location: {location}, temperature: {temperature}")
        return data
    else:
        print("Failed to fetch data:", res.status_code)


if __name__ == "__main__":
    get_weather()
