import os

import requests

API_KEY = os.getenv("API_KEY")

if not API_KEY:
    raise ValueError("A variável de ambiente API_KEY é obrigatória")

BASE_URL = "http://api.weatherapi.com/v1/current.json"
CITY = "Paris"

response = requests.get(
    f"{BASE_URL}?key={API_KEY}&q={CITY}"
)
response.raise_for_status()

data = response.json()

print(f"Cidade: {data['location']['name']}")
print(f"Temperatura: {data['current']['temp_c']}°C")
print(f"Clima: {data['current']['condition']['text']}")
