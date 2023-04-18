FROM python:3.10.7-slim
LABEL maintainer="yuliamala44@gmail.com"
ENV PYTHONUNBUFFERED 1
WORKDIR app/
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY . .
CMD ["python", "app/main.py"]
