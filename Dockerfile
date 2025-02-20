# Use a small base image
FROM python:3.11-slim

# Disable output buffering
ENV PYTHONUNBUFFERED=1

# Set working directory
WORKDIR /app

# Copy and install dependencies
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY . .

# Set the default command to execute the script
CMD ["python", "app/main.py"]
