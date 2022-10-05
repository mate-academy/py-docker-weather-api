FROM python:3.10.4-alpine
LABEL maintainer="pavlejviki@gmail.com"

ENV PYTHONUNBUFFERED 1

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

WORKDIR app/

COPY . .

CMD ["python", "app/main.py"]
