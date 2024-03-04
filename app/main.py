from __future__ import print_function
import requests


# http://api.weatherapi.com/v1/search.json?key=1a89060c76a14afba95134309242702&q=Paris

def get_weather() -> None:
    url = "http://api.weatherapi.com/v1/current.json?"
    work_key = "1a89060c76a14afba95134309242702"
    work_sity = "Paris"
    work_params = f"key={work_key}&q={work_sity}"

    work_request = requests.get(url, params=work_params)

    if work_request.status_code != 200:
        print(f"Error request: {work_request.status_code}")

    result = work_request.json()

    test_view = f"Local time: {result['location']['localtime']}, temp(C): {result['current']['temp_c']}, precipitation: {result['current']['condition']['text']}, wind(m/c): {result['current']['wind_mph']}, direction wind: {result['current']['wind_dir']}"

    ttt = 0


if __name__ == "__main__":
    get_weather()
