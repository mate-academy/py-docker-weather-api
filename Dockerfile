# Use official Python image as base
FROM python:3.13-slim

# Set working directory
WORKDIR /app

# Copy requirements and install dependencies
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY app/ ./app/

# Set environment variable for Python
ENV PYTHONUNBUFFERED=1

# Set default command
CMD ["python", "app/main.py"]
