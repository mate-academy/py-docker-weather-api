FROM python:3.11
LABEL maintainer="mate-academy"

WORKDIR /app

COPY . .

RUN pip install -r requirements.txt

CMD [ "python", "main.py" ]