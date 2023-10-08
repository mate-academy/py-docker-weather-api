FROM python:3.11.1-alpine

LABEL maintainer="olehoryshshuk@gmail.com"

ENV PYTHONUNBUFFERED 1

WORKDIR weather/

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .

CMD ["python", "app/main.py"]