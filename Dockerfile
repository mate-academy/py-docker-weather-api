FROM python:3.14.7-alpine3.24
LABEL maintainer="mikhailetc.artem@gmail.com"

ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .

EXPOSE 8000

CMD ["python", "app/main.py"]