FROM python:3.9-alpine
LABEL maintainer="nikulicastas2004@gmail.com"

ENV PYTHONUNBUFFERED 1
ENV WEATHER_API_KEY None
ENV CITY None

WORKDIR app/

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .

CMD ["python", "app/main.py"]
