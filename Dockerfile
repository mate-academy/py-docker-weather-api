FROM python:3.10.11-slim
LABEL maintaner="phaishuk"
ENV PYTHONBUFFERED 1
WORKDIR root/
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY . .
CMD ["python","./app/main.py","get_weather"]
