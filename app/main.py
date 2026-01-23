import os
import sys
import requests

def get_weather():
    # 1. Get API Key from Environment Variable
    api_key = os.environ.get("API_KEY")
    if not api_key:
        print("Error: API_KEY environment variable not set.")
        sys.exit(1)

    city = "Paris"
    base_url = "http://api.weatherapi.com/v1/current.json"
    
    # 2. Print the "Performing request..." line as shown in the task
    print(f"Performing request to Weather API for city {city}...")

    try:
        response = requests.get(f"{base_url}?key={api_key}&q={city}")
        response.raise_for_status()
        data = response.json()

        # 3. Extract data to match the screenshot format:
        # "Paris/France 2022-06-14 11:55 Weather: 22.0 Celsius, Sunny"
        location = data['location']['name']
        country = data['location']['country']
        local_time = data['location']['localtime']
        temp_c = data['current']['temp_c']
        condition = data['current']['condition']['text']

        print(f"{location}/{country} {local_time} Weather: {temp_c} Celsius, {condition}")

    except requests.exceptions.RequestException as e:
        print(f"Error fetching weather data: {e}")

if __name__ == "__main__":
    get_weather()
