FROM python:3.12.2-slim
LABEL maintaner="jaegarn141@gmail.com"

ENV PYTHOUNNBUFFERED 1

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .

CMD ["python", "-m", "app.main"]