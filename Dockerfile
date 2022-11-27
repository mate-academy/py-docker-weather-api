FROM python:3.10-slim-buster
LABEL maintaner="oliatrofymchuk@knu.ua"

ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .

CMD ["python", "app/main.py"]
