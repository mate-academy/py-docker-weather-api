FROM python:3.12-slim
LABEL maintainer="Konstantin-SVT"

ENV PYTHONUNBUFFERED=1

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .
WORKDIR app
ENTRYPOINT ["python", "main.py"]