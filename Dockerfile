FROM python:3.12-slim
LABEL maintainer="nadiia.developer777@gmail.com"

ENV PYTHONUNBUFFERED 1

WORKDIR code/

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

COPY . .

ENV API_KEY = "372c2f4a2c3d4a94b8a164824241701"

CMD ["python", "app/main.py", "runserver", "0.0.0.0:8000"]
