# Use minimal Python base image
FROM python:3.10-slim
LABEL maintainer="turulko"
# Set working directory
WORKDIR /app

# Copy only requirements first (for caching)
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy project files
COPY app/ ./app/

# Set entrypoint
CMD ["python", "app/main.py"]
