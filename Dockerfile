FROM python:3.11-slim
LABEL manufacturer="polyakovv.andrey@gmail.com"

ENV API_KEY "7c6ae753b9a04fe6af8124602231001"

WORKDIR app/

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .

CMD ["python", "app/main.py"]