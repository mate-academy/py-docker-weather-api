import requests
import json
import dotenv
import os


def get_weather() -> None:
    dotenv.load_dotenv()
    res = requests.get(
        f"http://api.weatherapi.com/v1/current.json?key="
        f"{os.getenv('API_KEY')}&q=Paris"
    )
    if res.status_code == 200:
        res = json.loads(res.content)
        print(
            f"Performing request to Weather API for city Paris:\n"
            f"Paris/France {res['location']['localtime']} Weather: "
            f"{res['current']['temp_c']} Celsius, "
            f"{res['current']['condition']['text']}"
        )
    else:
        print("Request was not successful. Status code: " + str(res.status_code))


if __name__ == "__main__":
    get_weather()
