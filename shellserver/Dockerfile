# Dockerfile
# Use an official Python runtime as a parent image
FROM python:3.12-slim-bookworm

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Install system dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    curl \
    ca-certificates \
    gnupg \
    dirmngr \
 && update-ca-certificates \
 && apt-get clean \
 && rm -rf /var/lib/apt/lists/*

 # Add your corporate root certificate to the container's trusted CA store
COPY Zscaler-Root-CA.pem /usr/local/share/ca-certificates/Zscaler-Root-CA.crt
RUN update-ca-certificates

# Set the working directory in the container
WORKDIR /app

# Install dependencies
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY server.py ./

# Define the command to run the application using 'uv run'
CMD ["python", "server.py"]