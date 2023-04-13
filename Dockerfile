FROM python:3.10-slim
LABEL maintainer="foksanv@gmail.com"

ENV PYTHONUNBUFFERED 1

WORKDIR app/

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

ENV API_KEY=${API_KEY}

COPY . .

CMD ["python", "app/main.py"]