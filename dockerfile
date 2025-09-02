FROM python:3.11-slim

WORKDIR /app

# Install libmagic and clean up apt cache
RUN apt-get update && apt-get install -y --no-install-recommends \
    libmagic1 \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY axur-feed.py manifest.json ./

CMD ["python", "axur-feed.py"]
