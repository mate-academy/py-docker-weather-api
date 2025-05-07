FROM python:3.11-slim

WORKDIR /weather_app

COPY requirements.txt /weather_app/

RUN pip install --no-cache-dir -r requirements.txt

COPY app /weather_app/

CMD ["python", "weather_app/app/main.py"]
