FROM python:3.13-alpine


ENV PYTHONUNBUFFERED=1

WORKDIR "weather_project/"

COPY requirements.txt requirements.txt

RUN pip install --no-cache -r requirements.txt

COPY . .

CMD ["python", "app/main.py"]