from __future__ import print_function
import os
import weatherapi
from weatherapi.rest import ApiException
from dotenv import load_dotenv

load_dotenv()


def get_weather():
    # Configure API key authorization: ApiKeyAuth
    configuration = weatherapi.Configuration()
    configuration.api_key["key"] = os.getenv("WEATHER_API_KEY")
    # Uncomment below to set up prefix (e.g. Bearer) for API key, if needed
    # configuration.api_key_prefix['key'] = 'Bearer'

    # create an instance of the API class
    api_instance = weatherapi.APIsApi(weatherapi.ApiClient(configuration))
    q = "Paris"  # str | Pass US Zipcode,
    # UK Postcode, Canada Postalcode,
    # IP address, Latitude/Longitude (decimal degree) or city name.
    # Visit [request parameter section]
    # (https://www.weatherapi.com/docs/#intro-request) to learn more.

    try:
        api_response = api_instance.realtime_weather(q)
        data = api_response
        location = data["location"]
        current = data["current"]
        condition = current["condition"]

        print(
            f"🌍 Location: {location['name']}, "
            f"{location['region']}, "
            f"{location['country']}"
        )
        print(f"🕒 Local Time: {location['localtime']}")
        print(
            f"🌡️ Temperature: {current['temp_c']}°C"
            f" (Feels like {current['feelslike_c']}°C)"
        )
        print(f"💧 Humidity: {current['humidity']}%")
        print(f"💨 Wind: {current['wind_kph']} kph ({current['wind_dir']})")
        print(f"🌦️ Condition: {condition['text']}")
    except ApiException as e:
        print("Exception when calling APIsApi->astronomy: %s\n" % e)


if __name__ == "__main__":
    get_weather()
