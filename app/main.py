import requests

from rest_framework import status


def get_weather() -> None:
    api_key = "6f5034b237604c6095f61436230602"
    city_name = "Paris"
    url = f"https://api.weatherapi.com/v1/current.json?key=" \
          f"{api_key}&q={city_name}&aqi=no"
    complete_url = url

    # get method of requests module
    # return response object
    response = requests.get(complete_url)

    # Check the status code of response
    if response.status_code != status.HTTP_403_FORBIDDEN:
        # json method of response object
        # convert json format data into
        # python format data
        weather_list = response.json()

        # Now weather_list contains list of nested dictionaries
        current = weather_list.get("current")
        city = f"City: {weather_list.get('location').get('name')}"
        temp_c = f"Temperature C : {current.get('temp_c')}"
        temp_f = f"Temperature F: {current.get('temp_f')}"
        condition = f"Condition : {current.get('condition').get('text')}"
        wind = f"Wind : {current.get('wind_mph')}"

        print(f"""The weather
        {city}
        {temp_c}
        {temp_f}
        {condition}
        {wind}""")
    else:
        print(" Bad request ")


if __name__ == "__main__":
    get_weather()
