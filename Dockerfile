FROM python:3.11.4
LABEL maintainer="tina.vasylenko@gmail.com"

WORKDIR app/

COPY requirements.txt requirements.txt

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["python", "app/main.py"]
