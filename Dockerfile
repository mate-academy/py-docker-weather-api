FROM python:3.10.5-slim
LABEL maintainer="davidkrivko@gmail.com"

ENV PYTHONUNBUFFERED 1

WORKDIR weather/

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .

CMD ["python", "weather/main.py"]
