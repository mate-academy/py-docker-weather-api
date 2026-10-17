FROM python:3.15-alpine3.24
ENV PYTHONUNBUFFERED=1
WORKDIR /app
COPY requirements_docker.txt .
RUN pip install --no-cache-dir -r requirements_docker.txt
COPY . .
EXPOSE 8000
CMD ["python", "app/main.py"]