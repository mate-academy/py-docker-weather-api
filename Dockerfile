FROM python:3.10.10-slim
LABEL maitainer="shatrovskyi.vlad@gmail.com"

ENV PYTHONUNBUFFERED 1

WORKDIR /usr/src/app

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .

CMD ["python", "app/main.py"]
