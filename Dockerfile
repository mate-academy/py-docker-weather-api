FROM python:3.11-alpine
LABEL authors="lotrikys@gmail.com"

WORKDIR app/

ADD app/main.py .
ADD requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

CMD ["python", "main.py"]
