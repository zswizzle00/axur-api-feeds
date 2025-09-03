FROM python:3.11-slim

# Install system dependencies including libmagic
RUN apt-get update && apt-get install -y \
    libmagic1 \
    gcc \
    && rm -rf /var/lib/apt/lists/*

# Set working directory
WORKDIR /app

# Copy requirements first for better caching
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the connector code
COPY axur-feed.py .

# Run the connector
CMD ["python", "axur-feed.py"]
