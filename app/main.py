from requests import get

from constants import BASE_URL, API_KEY


def get_weather(city: str) -> None:

    weather = get(BASE_URL, {
        "key": API_KEY,
        "q": city,
    }).json()

    city = weather["location"]["name"]
    country = weather["location"]["country"]
    date = weather["location"]["localtime"]
    temperature = weather["current"]["temp_c"]
    condition = weather["current"]["condition"]["text"]

    print(f"Country: {country}. City: {city}. Date: {date}")
    print(f"Temperature: {temperature}, Condition: {condition}")


if __name__ == "__main__":
    get_weather("PARIS")
