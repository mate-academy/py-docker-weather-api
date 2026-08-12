import requests
import os


def get_weather() -> None:
    api_key = os.getenv("API_KEY")

    url = "https://api.weatherapi.com/v1/current.json?"
    payload = {
        "q": "Paris",
        "aqi": "no",
        "pollen": "no",
        "lang": "string",
        "current_fields": "string"
    }

    try:
        response = requests.get(
            url,
            params=payload,
            headers={
                "key": api_key,
            }

        )

        # Check responce status code (status-code 200 OK)
        # If we get an errer (ex, 404 or 500), rising exception
        print("Performing request to Whether API for city Paris...")
        response.raise_for_status()

        # Parsing JSON to Python Dict
        data = response.json()

        print(
            f"{data["location"]["name"]}/{data["location"]["country"]} "
            f"{data["location"]["localtime"]} "
            f"Wether: {data["current"]["temp_c"]} "
            f"Celcius, {data["current"]["condition"]["text"]}"
        )

    except requests.exceptions.RequestException as e:
        print(f"Get an error while trying connect to API: {e}")


if __name__ == "__main__":
    get_weather()
