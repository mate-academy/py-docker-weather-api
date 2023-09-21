import os
import requests
import logging

# Set up logging
logging.basicConfig(level=logging.INFO, format="%(message)s")
logger = logging.getLogger(__name__)


def get_api_key() -> str:
    """Get the API_KEY from environment variables."""
    api_key = os.environ.get("API_KEY")
    if not api_key:
        logger.error("API_KEY environment variable is not set.")
    return api_key


def get_weather() -> None:
    """Get current weather for Paris city"""
    url = "http://api.weatherapi.com/v1/current.json"
    filtering = "Paris"

    api_key = get_api_key()

    if not api_key:
        return  # Exit gracefully if API_KEY is missing.

    try:
        response = requests.get(url, params={"q": filtering, "key": api_key})

        if response.status_code == 200:
            data = response.json()
            location = (
                f"{data['location']['name']}/"f"{data['location']['country']}"
            )
            local_time = data["location"]["localtime"]
            temperature = data["current"]["temp_c"]
            condition = data["current"]["condition"]["text"]

            logger.info(
                f"{location} {local_time} "
                f"Weather: {temperature}°C, {condition}"
            )
        else:
            logger.error(
                f"API request failed with status code {response.status_code}"
            )
    except requests.exceptions.RequestException as e:
        logger.error(f"Failed to make API request: {e}")
    except ValueError as e:
        logger.error(f"Failed to parse API response as JSON: {e}")


if __name__ == "__main__":
    get_weather()
