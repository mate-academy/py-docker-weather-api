FROM python:3.10.7
LABEL maintaner="olha.tryhub@nure.ua"

ENV PYTHONBUFFERRED 1

WORKDIR app/

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .

CMD ["python", "app/main.py"]