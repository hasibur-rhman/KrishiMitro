FROM python:3.11-slim

WORKDIR /app

# Install system utilities
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Copy backend requirements and install
COPY backend/requirements.txt ./backend/
RUN pip install --no-cache-dir -r backend/requirements.txt

# Copy all project files
COPY . .

# Environment defaults
ENV PYTHONUNBUFFERED=1
ENV PORT=8000

# Expose standard web port
EXPOSE 8000

# Run knowledge-base ingestion on container startup if needed, then run FastAPI via Uvicorn
WORKDIR /app/backend
CMD ["sh", "-c", "python -m app.rag.ingest && uvicorn app.main:app --host 0.0.0.0 --port ${PORT:-8000}"]
