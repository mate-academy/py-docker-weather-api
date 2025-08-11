FROM python:3.12.11-slim
LABEL maintainer="dimkanividimka@gmail.com"
ENV PYTHONUNBUFFERED 1
WORKDIR app/
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY . .
CMD ["python", "app/main.py"]