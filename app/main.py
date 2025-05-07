import os
import requests


def get_weather(api_key: str) -> None:

    url = "http://api.weatherapi.com/v1/current.json"
    params = {"key": api_key, "q": "Paris"}

    response = requests.get(url, params=params)

    if response.status_code == 200:
        data = response.json()
        city = data["location"]["name"]
        country = data["location"]["country"]
        local_time = data["location"]["localtime"]
        temp_c = data["current"]["temp_c"]
        condition = data["current"]["condition"]["text"]
        return (f"{city}/{country} {local_time} "
                f"Weather: {temp_c} Celsius, {condition}")
    else:
        return f"Error : {response.status_code} - {response.text}"


if __name__ == "__main__":

    api_key = os.getenv("API_KEY")
    if not api_key:
        raise ValueError("API_KEY is not set in environment variables")

    print(get_weather(api_key))
