FROM python:3.11-alpine
LABEL maintainer="starcrafter4444@gmail.com"

ENV PYTHONUMBUFFERED 1

WORKDIR app/

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .

CMD ["python", "app/main.py"]
