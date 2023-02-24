import requests


def get_weather() -> None:
    api_key = "0ea52d0f1b41445ab60115328232302"
    url = "http://api.weatherapi.com/v1/current.json?key="
    aqi = "no"
    city_name = "Paris"
    full_url = url + api_key + "&q=" + city_name + "&aqi=" + aqi
    req = requests.get(full_url)
    info = req.json()
    print(
        f"{info['location']['name']}/{info['location']['country']} "
        f"{info['location']['localtime']} "
        f"Weather: {info['current']['temp_c']} Celsius, "
        f"{info['current']['condition']['text']}"
    )


if __name__ == "__main__":
    get_weather()
