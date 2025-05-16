FROM python:3.12-slim

# Set working directory
WORKDIR /app

# Copy only necessary files
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY app/ ./app/

# Set the default command
CMD ["python", "app/main.py"]
