import requests
import os


class ApiError(Exception):
    def __init__(self, code: int, message: str) -> None:
        self.code = code
        self.message = message
        super().__init__(message)


def get_weather(
        requested_info: str,
        q_param: str
) -> None:
    base_url = "http://api.weatherapi.com/v1"
    api_key = os.getenv("API_KEY")
    if not api_key:
        raise ApiError(400, "You should provide the API KEY.")
    response = requests.get(
        f"{base_url}/{requested_info}",
        params={"key": api_key, "q": q_param}
    )
    if response.status_code != 200:
        data = response.json()
        print(data)
        if "error" in data:
            raise ApiError(
                data["error"].get("code"),
                data["error"].get("message")
            )
        raise ApiError(response.status_code, "Check your code for errors!")

    print(response.text)


if __name__ == "__main__":
    try:
        get_weather("current.json", "Paris")
    except ApiError as e:
        print(f"{e.code} {e.message}")
