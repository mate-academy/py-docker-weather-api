FROM python:3.11-slim
LABEL maintainer="viktoria.om@gmail.com"
ENV PYTHONBUFFERED=1
WORKDIR /app
COPY . .
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

CMD ["python", "app/main.py"]
