FROM python:3.10.8-slim
LABEL maintainer = "tanyakozakova"

ENV PYTHONUNBUFFERED 1
ENV API_KEY "d4e3e1249ff546a39b2121545230507"

WORKDIR app/

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .

CMD ["python", "app/main.py", "0.0.0.0:8000"]
