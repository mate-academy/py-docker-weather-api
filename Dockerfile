FROM python:3.11
LABEL maintainer="catsperr322@gmail.com"

ENV PYTHONBUFFERED 1

WORKDIR /app/src/

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .

CMD ["python", "app/main.py"]
