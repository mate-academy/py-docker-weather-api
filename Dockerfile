FROM python:3.11-alpine

WORKDIR /app

COPY . .

RUN pip install -r requirements.txt 

CMD ["python", "app/main.py"]

ENV API_URL=http://api.weatherapi.com/v1/current.json?
