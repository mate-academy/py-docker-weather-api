import requests
import os


URL = "http://api.weatherapi.com/v1/current.json?"
FILTERING = "Kyiv"


def get_weather() -> str:

    response = requests.get(URL + f"key={os.environ.get("API_KEY")}&q={FILTERING}")

    if response.status_code == 200:
        data = response.json()
        print(
            f"location: {data["location"]["name"]}, "
            f"temperature: {data["current"]["temp_c"]}"
        )
        return data
    else:
        print("Failed to fetch data:", response.status_code)
        return None


if __name__ == "__main__":
    get_weather()
