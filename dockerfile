FROM python:3.11-slim

WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY axur-feed.py manifest.json ./

CMD ["python", "axur-feed.py"]
