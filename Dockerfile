FROM python:3.11.6-slim
LABEL maintainer="arturjust88@gmail.com"

ENV PYTHONUNBUFFERED 1
ENV API_KEY=abc123

WORKDIR app/

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .

CMD ["python", "app/main.py"]
