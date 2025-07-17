import requests
import os


def get_weather() -> None:
    url = "http://api.weatherapi.com/v1/current.json"
    api_key = os.environ.get("API_KEY")
    params = {
        "key": api_key,
        "q": "Paris",
    }

    response = requests.get(url, params=params)

    if response.status_code == 200:
        data = response.json()
        print(
            f"{data["Location"]["name"]}/{data["location"]["country"]} "
            f"{data["current"]["last_updated"]} "
            f"Weather: {data["current"]["temp_c"]} Celsius, "
            f"{data["current"]["condition"]["text"]}"
        )
    else:
        print("Error:", response.status_code, response.text)


if __name__ == "__main__":
    get_weather()
