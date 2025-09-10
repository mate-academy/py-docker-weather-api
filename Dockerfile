FROM python:3.12-slim
LABEL maintainer="serhiibasok@gmail.com"

WORKDIR /app

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

COPY app/ ./app/

CMD ["python", "app/main.py"]
