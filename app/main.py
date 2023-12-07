import os
import requests


def get_weather() -> None:
    api_key = os.getenv("API_KEY")
    response = requests.get(
        "https://api.weatherapi.com/v1/current.json?"
        f"key={api_key}&q=Paris"
    )
    if response.status_code == 200:
        response_json = response.json()
        print("The weather in Paris is : "
              f"{response_json['current']['temp_c']} degrees Celsius")
    else:
        print("An error occurred, try again later!")


if __name__ == "__main__":
    get_weather()
