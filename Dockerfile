FROM python:3.11-slim
LABEL maintainer="vladearth7@gmail.com"

ENV PYTHONUNBAFFERED 1

WORKDIR app/

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .

CMD [ "python", "app/main.py"]