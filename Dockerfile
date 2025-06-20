FROM python:3.12-slim
LABEL maintainer="kelor2@o2.pl"

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["python", "app/main.py"]