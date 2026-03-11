from dotenv import load_dotenv
import os
import requests


def get_weather() -> None:
    load_dotenv()

    api_key = os.getenv("API_KEY")
    url = os.getenv("URL")
    filtering = os.getenv("FILTERING")

    if not all([api_key, url, filtering]):
        print("Missing environment variables. Check -e flags.")
        return

    response = requests.get(f"{url}/current.json?key={api_key}&q={filtering}")
    print(response.json())


if __name__ == "__main__":
    get_weather()
