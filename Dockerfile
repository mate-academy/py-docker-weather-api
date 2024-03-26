FROM python:3.12.1-alpine
LABEL maintainer="kiyanitsa2002021@gmail.com"

ENV PYTHONUNBUFFERED 1

WORKDIR app/

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .

CMD ["python", "-m", "app.main"]
