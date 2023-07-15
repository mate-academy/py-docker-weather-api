FROM python:3.11.4-alpine
LABEL maintainer="Esxoyne@GitHub"

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .

CMD [ "python", "app/main.py" ]
