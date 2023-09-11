FROM python:3.9
LABEL maintainer="mishabenzel1997@gmail.com"

ENV PYTHONUNBUFFERED 1

WORKDIR weather_app/

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .
CMD ["python", "app/main.py"]
