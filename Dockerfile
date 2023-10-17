FROM python:3.11
LABEL maintainer="eduardhabryd@gmail.com"

WORKDIR /app

COPY . .

RUN pip install -r requirements.txt

CMD [ "python", "main.py" ]