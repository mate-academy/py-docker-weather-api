import os

import requests
from fastapi import FastAPI, HTTPException

app = FastAPI()

URL = "http://api.weatherapi.com/v1/current.json?"
API_KEY = os.environ.get("API_KEY")
CITY = "Paris"


@app.get("/weather")
def get_weather() -> any:
    if not API_KEY:  # Check if API_KEY is missing
        raise HTTPException(
            status_code=500,
            detail="API_KEY is missing. Set the environment variable."
        )
    response = requests.get(URL + f"key={API_KEY}&q={CITY}")

    if response.status_code != 200:  # if api_key is invalid
        return {"error": f"Failed to fetch weather data: {response.text}"}
    data = response.json()
    if "location" in data and "name" in data["location"]:
        location_name = data["location"]["name"]
    else:
        return {"error": "Invalid response structure", "raw_data": data}
    temperature = data["current"]["temp_c"]
    condition = data["current"]["condition"]["text"]

    return {
        "city": location_name,
        "temperature": temperature,
        "condition": condition
    }
