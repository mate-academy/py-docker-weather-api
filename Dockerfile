FROM python:3.12.10-alpine3.21
LABEL maintainer="yaroslav.zhuravlov.dev@gmail.com"

WORKDIR app
COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

COPY . .

CMD ["python", "app/main.py"]
