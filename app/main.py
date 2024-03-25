import requests
import os


URL = "http://api.weatherapi.com/v1/current.json?"
FILTERING = "Kyiv"


def get_weather() -> str:

    response = requests.get(
        URL + f"key={os.environ.get("API_KEY")}&q={FILTERING}"
    )

    if response.status_code == 200:
        data = response.json()
        location = data["location"]["name"]
        temperature = data["current"]["temp_c"]

        print(f"location: {location}, temperature: {temperature}")
        return data
    else:
        print("Failed to fetch data:", response.status_code)


if __name__ == "__main__":
    get_weather()
