FROM python:3.10.8-alpine
LABEL authors="solal"

ENV PYTHONUNBUFFERED=1

WORKDIR src/

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .

CMD ["python", "-m", "app.main"]