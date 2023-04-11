import requests


def get_weather():
    api_key = "b54a45c623e74410aed183111231004"
    url = f"http://api.weatherapi.com/v1/current.json?key={api_key}&q=Paris&lang=en"

    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()

        location = data["location"]["name"]
        temperature = data["current"]["temp_c"]
        condition = data["current"]["condition"]["text"]
        print(f"The weather in {location} is {temperature}°C and {condition}")
    else:
        print("Error: Could not retrieve weather data")


if __name__ == "__main__":
    get_weather()
