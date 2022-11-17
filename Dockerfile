FROM python:3.10.4-slim
LABEL maintainer="artemkazakov947@gmail.com"

ENV PYTHONUNBUFFERED 1

WORKDIR app/

COPY requirements.txt requirements.txt
RUN pip install -r requerements.txt

COPY . .

CMD ["python", "app/main.py"]
