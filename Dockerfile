FROM python:3.12-slim
LABEL maintainer="ztkkre@gmail.com"

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY app/main.py .

CMD ["python", "main.py"]