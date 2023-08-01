FROM python:3.11-slim
LABEL maintainer="mezismezis@gmail.com"

ENV PYTHONUNBUFFERED 1
ENV API_KEY 4ba7132a982a47bb93f85555230108

WORKDIR app/

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .

CMD ["python", "app/main.py"]