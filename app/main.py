import os
import requests


def get_weather() -> None:
    base_url = "https://api.weatherapi.com/v1/current.json?"
    api_key = os.getenv("API_KEY")

    city = "Paris"

    try:
        url = base_url + "key=" + api_key + "&q=" + city
        response_json = requests.get(url).json()
    except:
        raise EnvironmentError(
            "Set your environment variable API_KEY "
            "in terminal and run this script again"
        )

    result = (
        f"{city}/{response_json['location']['country']} "
        f"{response_json['location']['localtime']} "
        f"Weather: {response_json['current']['temp_c']} Celsius, "
        f"{response_json['current']['condition']['text']}"
    )
    print(result)


if __name__ == "__main__":
    get_weather()
