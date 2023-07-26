FROM python:3.9.0-slim
LABEL maintainer="1208petrova@gmail.com"

ENV PYTHONUNBEFFERED 1

WORKDIR app/

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .

CMD ["python", "app/main.py"]
