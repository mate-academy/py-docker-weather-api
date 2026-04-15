import os
import requests


CITY = "Paris"
URL = "http://api.weatherapi.com/v1/current.json"


def get_weather() -> None:
    api_key = os.environ.get("API_KEY")
    if not api_key:
        raise SystemExit("API_KEY is required")
    params = {"key": api_key, "q": CITY}
    try:
        resp = requests.get(URL, params=params, timeout=10)
        resp.raise_for_status()
    except requests.RequestException as e:
        print("Request error", e)
        raise SystemExit(1)

    data = resp.json()
    loc = data.get("location", {})
    cur = data.get("current", {})
    name = loc.get("name")
    country = loc.get("country")
    localtime = loc.get("localtime")
    temp = cur.get("temp_c")
    cond = cur.get("condition", {}).get("text")
    print(f"{name}/{country} {localtime} Weather: {temp} Celsius, {cond}")


if __name__ == "__main__":
    get_weather()
