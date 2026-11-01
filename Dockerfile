FROM python:3.10.8-slim
LABEL maintainer="andrii.hrabovskyi.one@gmail.com"

ENV PYTHONUNBUFFERED 1

WORKDIR app/

COPY app/main.py .
RUN pip install requests


CMD ["python", "main.py"]
