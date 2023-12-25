FROM python:3.10.8-slim
LABEL authors="laskarj"

ENV PYTHONUNBUFFERED 1

WORKDIR app/

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY ./app/main.py .

CMD ["python", "main.py"]
