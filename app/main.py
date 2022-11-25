import os

import requests

BASE_URL = "http://api.weatherapi.com/v1/current.json?key="
API_KEY = os.environ.get("API_KEY")


def get_weather() -> None:
    print("Welcome to the Docker Weather API")
    city = input("Type your city: ")
    information = input(
        f"Type 1 to see all or 2 to see short info "
        f"about the weather in {city}: "
    )
    print(f"Performing request to Weather API for city {city}...")

    url = BASE_URL + API_KEY + "&q=" + city
    result = requests.get(url)

    if result.status_code == 200:
        response = result.json()

        if information == "1":
            for key, values in response.items():
                print(f"{str(key).upper()}:")

                for value_key, value in values.items():
                    print(f"    {value_key}: {value}")

        if information == "2":
            city = response["location"]["name"]
            country = response["location"]["country"]
            localtime = response["location"]["localtime"]
            temp_c = response["current"]["temp_c"]
            condition = response["current"]["condition"]["text"]

            print(
                f"{city}/{country} {localtime} "
                f"Weather: {temp_c} Celsius, {condition}"
            )

    else:
        print(f"Error! Status code: {result.status_code}")


if __name__ == "__main__":
    get_weather()
