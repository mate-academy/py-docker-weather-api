FROM python:3.11.4-slim
LABEL maintainer="sashajanchuck13@gmail.com"

ENV PYTHONUNBUFFERD 1

WORKDIR app/

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .

CMD ["python", "app/main.py", "0.0.0.0:8000"]
