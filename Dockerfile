FROM python:3.10.1-slim-buster
LABEL maintainer="vasia_pupkin@pupkin.com"

ENV PYTHONUNBUFFERED 1

WORKDIR app/

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .

CMD ["python", "app/main.py"]