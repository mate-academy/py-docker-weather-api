# Use official lightweight Python image
FROM python:3.9-slim

# Set working directory
WORKDIR /app

# Copy only necessary files
COPY app/main.py .

# Install required package
RUN pip install --no-cache-dir requests

# Run the application
CMD ["python", "main.py"]
