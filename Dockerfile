FROM python:3.10.4-alpine
LABEL maintainer="alexzubkoff123@gmail.com"

ENV PYTHONUNBUFFERED 1
ENV API_KEY=8b89884a56104151964200013222711

WORKDIR app/

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .

CMD [ "python", "./app/main.py"]
