FROM python:3.11-slim
LABEL maintainer="viktoriakalinina@orderberry.de"
ENV PYTHONUNBURFFERED 1
WORKDIR /app
COPY requirements.txt requirements.txt
RUN pip install --no-cash-dir -r requirements.txt
COPY . .
CMD ["python", "app/main.py"]
