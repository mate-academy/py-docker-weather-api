FROM python:3.12-alpine

ENV PYTHOUNNBUFFERED 1

WORKDIR app/

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

ENV API_KEY=$API_KEY

COPY . .

CMD ["python", "app/main.py"]
