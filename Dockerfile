FROM python:3.11-slim
LABEL manufacturer="polyakovv.andrey@gmail.com"

WORKDIR app/

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .

CMD ["python", "app/main.py"]
