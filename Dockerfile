FROM python:3.11-slim
LABEL maintainer="rinoto.kun@gmail.com"

ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY docker_requirements.txt docker_requirements.txt
RUN pip install -r docker_requirements.txt

COPY . .

CMD ["python", "app/main.py"]
