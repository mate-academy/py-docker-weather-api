FROM python:3.11-slim
LABEL maintainer="eduardhabryd@gmail.com"

ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY . .

RUN pip install -r requirements.txt

CMD [ "python", "app/main.py" ]
