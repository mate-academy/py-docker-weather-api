import requests
import os


def get_weather() -> None:
    url = (
        "http://api.weatherapi.com/v1/current.json"
        f"?key={os.environ.get('API_KEY')}=Paris"
    )
    res = requests.get(url)
    if res.status_code == 200:
        temp_c = res.json().get("current").get("temp_c")
        temp_f = res.json().get("current").get("temp_f")
        last_updated = res.json().get("current").get("last_updated")
        print(
            "Current temperature in Paris: "
            f"{temp_c} C, {temp_f} F (last updated: {last_updated})"
        )
    else:
        print(f"There is {res.status_code} error with your request")


if __name__ == "__main__":
    get_weather()
