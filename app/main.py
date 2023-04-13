import os

import requests


def get_weather() -> None:
    # Define the API endpoint and parameters
    url = "https://api.weatherapi.com/v1/current.json"
    api_key = os.environ.get("API_KEY")
    params = {
        "key": api_key,  # Replace with your WeatherAPI API key
        "q": "Paris",  # Specify the location as Paris
    }

    # Send a GET request to the WeatherAPI
    response = requests.get(url, params=params)
    # print(response.status_code)

    # Check if the request was successful
    if response.status_code == 200:
        # Parse the JSON response
        data = response.json()

        # Extract the relevant information
        city = data["location"]["name"]
        country = data["location"]["country"]
        temperature = data["current"]["temp_c"]
        condition = data["current"]["condition"]["text"]

        # Print the current weather information
        print(f"Current weather in {city}, {country}:")
        print(f"Temperature: {temperature}°C")
        print(f"Condition: {condition}")
    else:
        print("Failed to retrieve weather data. Please check your API key and try again.")


if __name__ == "__main__":
    get_weather()
