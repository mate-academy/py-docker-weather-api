FROM python:3.12.1-slim-bullseye
LABEL maintainer="knyrikkolesnichenko2004@gmail.com"

ENV PYTHONBUFFERED 1

WORKDIR app/

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .

CMD ["python", "app/main.py"]
