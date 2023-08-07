FROM python:3.11.4-alpine3.17
LABEL maintainer="kannabis252@gmail.com"

ENV PYTHONUNBUFFERED 1

WORKDIR app/

COPY . .
RUN pip install -r requirements.txt


CMD ["python", "app/main.py"]
