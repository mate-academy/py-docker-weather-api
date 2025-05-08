import weatherapi
from weatherapi.rest import ApiException

import os


API_KEY = os.environ.get("API_KEY")
QUERY = "Paris"
DAYS = 1


def get_weather() -> None:
    configuration = weatherapi.Configuration()
    if API_KEY is None:
        print("No API key provided.")
        return
    configuration.api_key["key"] = API_KEY

    # creating an instance of the API class
    api_instance = weatherapi.APIsApi(weatherapi.ApiClient(configuration))

    try:
        # forecast API
        api_response = api_instance.forecast_weather(QUERY, DAYS)

        current_weather = api_response.get("current", dict())
        location = api_response.get("location", dict())

        city = location.get("name", "Unknown")
        country = location.get("country", "Unknown")

        update_date = current_weather.get("last_updated", "Unknown")
        weather = (f"{current_weather.get("temp_c", "Unknown")} Celsius, "
                   f"{current_weather.get(  # noqa
                       "condition",
                       dict()
                   ).get("text", "Unknown")}")

        print(f"Performing request to Weather API "
              f"for city {city}...\n{city}/{country} "
              f"{update_date} Weather: {weather}")
    except ApiException as e:
        print(f"Exception when calling APIsApi->forecast_weather: {e}")


if __name__ == "__main__":
    get_weather()
