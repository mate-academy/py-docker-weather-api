FROM python:3.15.2
LABEL author="Mateusz"

ENV PYTHONUNBUFFERED=1

WORKDIR /App


COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

CMD ["python", "app/main.py", "runserver", "0.0.0.0:8000"]