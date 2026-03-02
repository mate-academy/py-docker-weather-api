# Base image
FROM python:3.13-slim

# Set working directory
WORKDIR /app

# Copy requirements file
COPY requirements.txt .

# Install dependencies without cache to keep image thin
RUN pip install --no-cache-dir -r requirements.txt

# Copy application files
COPY . .

# Command to run the application
CMD ["python", "app/main.py"]
