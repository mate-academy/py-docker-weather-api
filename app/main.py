import os
import requests


def get_weather() -> None:
    base_url = "https://api.weatherapi.com/v1/current.json?"
    api_key = os.getenv("API_KEY")

    city = "Seoul"

    if not os.getenv("API_KEY"):
        raise TypeError(
            "Set your environment variable API_KEY "
            "in terminal and run this script again"
        )

    url = base_url + "key=" + api_key + "&q=" + city

    try:
        requests.get(url).status_code == 200
    except ValueError:
        print("Invalid status code")

    response_json = requests.get(url).json()

    result = (
        f"{city}/{response_json['location']['country']} "
        f"{response_json['location']['localtime']} "
        f"Weather: {response_json['current']['temp_c']} Celsius, "
        f"{response_json['current']['condition']['text']}"
    )
    print(result)


if __name__ == "__main__":
    get_weather()
