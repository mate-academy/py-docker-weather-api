import requests
import os


def get_weather(key: str, city: str) -> str:
    url = "http://api.weatherapi.com/v1/current.json"
    data = requests.get(f"{url}?key={key}&q={city}")
    if data.status_code == 200:
        city_get = data.json()["location"]["name"]
        country = data.json()["location"]["country"]
        time = data.json()["location"]["localtime"]
        temp = data.json()["current"]["temp_c"]
        text = data.json()["current"]["condition"]["text"]
        return f"{city_get}/{country} {time} Weather: {temp}, Celsius, {text}"
    return f"You got {data.status_code}."


if __name__ == "__main__":
    api_key = os.getenv("API_KEY")
    if not api_key:
        print("API_KEY environment variable not set")
    print(get_weather(api_key, city="Paris"))
