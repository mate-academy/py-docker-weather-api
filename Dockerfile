FROM python:3.10.8-slim
LABEL author="vova.gld05@gamil.com"

ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

COPY ./app .

CMD ["python", "main.py"]