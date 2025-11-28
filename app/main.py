import os
import requests

API_URL = "http://api.weatherapi.com/v1/current.json"
CITY = "Paris"
AQI = "no"

def main():
    api_key = os.getenv("API_KEY")
    if not api_key:
        raise ValueError("API_KEY environment variable is not set")

    url = f"{API_URL}?key={api_key}&q={CITY}&aqi={AQI}"

    response = requests.get(url)
    data = response.json()

    print("Weather in Paris:")
    print(f"Temperature: {data['current']['temp_c']}°C")
    print(f"Condition: {data['current']['condition']['text']}")
    print(f"Wind: {data['current']['wind_kph']} kph")

if __name__ == "__main__":
    main()
