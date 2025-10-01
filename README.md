Weather Paris (Docker + WeatherAPI)

Script simples (flake8-compliant) que imprime o clima atual de Paris usando a WeatherAPI.
Empacotado em Docker com imagem python:3.12-slim.

Requisitos

Python 3.12+ (opcional, só para rodar local)

Conta e API key da WeatherAPI

Docker Desktop

Estrutura
.
├─ app/
│  └─ main.py
├─ requirements.txt
├─ .dockerignore
└─ Dockerfile

Ambiente

Defina a variável de ambiente API_KEY com a sua chave da WeatherAPI.

Rodar local (sem Docker)

Windows (PowerShell)

$env:API_KEY = "SUA_CHAVE_WEATHERAPI"
python app/main.py


macOS/Linux (bash)

export API_KEY="SUA_CHAVE_WEATHERAPI"
python app/main.py

Docker — Build e Run
Build
docker build -t weather-paris:latest .

Executar (passando API_KEY)

Windows (PowerShell)

$env:API_KEY = "SUA_CHAVE_WEATHERAPI"
docker run --rm -e API_KEY=$env:API_KEY weather-paris:latest


macOS/Linux (bash)

export API_KEY="SUA_CHAVE_WEATHERAPI"
docker run --rm -e API_KEY=$API_KEY weather-paris:latest


Saída esperada (exemplo):

Paris, France: 18.2°C (feels 18.0°C), Partly cloudy. Humidity 60%, wind 12.2 kph.

Publicar no Docker Hub
Login
docker login

Tag
docker tag weather-paris:latest SEU_USUARIO/weather-paris:latest

Push
docker push SEU_USUARIO/weather-paris:latest

Usar a imagem do Docker Hub
docker pull SEU_USUARIO/weather-paris:latest
docker run --rm -e API_KEY="SUA_CHAVE_WEATHERAPI" SEU_USUARIO/weather-paris:latest

Troubleshooting

“Missing API_KEY…” → a variável não foi passada ao container. Use -e API_KEY=....

HTTP 4xx/5xx → chave inválida/expirada, cota da API, ou problema temporário. Gere nova chave ou tente novamente.

Cannot connect to the Docker daemon → abra o Docker Desktop e aguarde “Running”.

Imagem desatualizada → rode o docker build novamente antes de docker run.

Notas de implementação

Base: python:3.12-slim

Dependência: requests>=2.32,<3

Leitura de configuração via variável de ambiente:

API_KEY (obrigatória)

Sem docker-compose (conforme requisitos).
