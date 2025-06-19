FROM python:3.13
LABEL maintainer="smolinskijmaksim1@gmail.com"

ENV PYTHONUNBUFFERED=1

WORKDIR /app/

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY ./app .
CMD ["python", "main.py"]