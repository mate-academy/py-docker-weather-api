FROM python:3.11.3-alpine
LABEL maintainer="bilmaxim@gmail.com"

ENV PYTHONUNBUFFERED=1

WORKDIR /weather-api/

COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD [ "python", "app/main.py" ]
