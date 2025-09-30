import requests, os
from dotenv import load_dotenv

def get_weather() -> None:
    # write your code here
    load_dotenv()
    response = requests.get("http://api.weatherapi.com/v1/current.json",
                            params={"key": os.environ["API_KEY"], "q": "Paris"})
    if response.status_code != 200:
        print("Error:", response.status_code, response.text)
    else:
        data = response.json()
        print(data)


if __name__ == "__main__":
    get_weather()
