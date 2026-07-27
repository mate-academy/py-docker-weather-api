FROM python:3.10.8-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY app/ ./app/

CMD ["python", "app/main.py"]

REQUIREMENTS.TXT:

flake8==5.0.4
flake8-annotations==2.9.1
flake8-quotes==3.3.1
flake8-variables-names==0.0.5
pep8-naming==0.13.2
requests==2.31.0