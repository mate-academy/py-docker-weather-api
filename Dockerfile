FROM python:3.10.8-slim
LABEL maintaner="spacix"
ENV PYTHONBUFFERED 1
#ENV API_KEY None
WORKDIR root/
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY . .
CMD ["python","./app/main.py","get_weather"]