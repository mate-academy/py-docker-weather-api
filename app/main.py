import requests
import os


def get_weather() -> None:
    # write your code here
    response = requests.get("http://api.weatherapi.com/v1/current.json",
                            params={"key": os.environ["API_KEY"],
                                    "q": "Paris"})
    if response.status_code != 200:
        print("Error:", response.status_code, response.text)
    else:
        data = response.json()
        print("Performing request to Weather API for city Paris...")
        print(f"{data['location']['name']}/{data['location']['country']} "
              f"{data['current']['last_updated']} "
              f"Weather: {data['current']['temp_c']} Celsius, "
              f"{data['current']['condition']['text']}")


if __name__ == "__main__":
    get_weather()
