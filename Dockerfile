# python base image
FROM python:3.12-slim

WORKDIR /app

RUN apt-get update && apt-get install -y git && apt-get clean

COPY . .

# install dependencies
RUN pip install --no-cache-dir -r requirements.txt

CMD ["python", "app/main.py"]