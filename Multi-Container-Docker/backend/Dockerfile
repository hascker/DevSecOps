############################
# Stage 1: Builder
############################
FROM python:3.11-slim AS builder

# Prevent Python from writing .pyc files
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /install

# System dependencies needed only for building wheels
RUN apt-get update && apt-get install -y --no-install-recommends \
    gcc \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Copy dependency list
COPY requirements.txt .

# Install dependencies cleanly and force correct versions
RUN pip install --upgrade pip \
    && pip install \
        --no-cache-dir \
        --upgrade \
        --force-reinstall \
        -r requirements.txt


############################
# Stage 2: Runtime
############################
FROM python:3.11-slim

# Create non-root user
RUN useradd --create-home appuser

WORKDIR /app

# Copy only installed Python packages from builder
COPY --from=builder /install /usr/local

# Copy application code
COPY app ./app

# Switch to non-root user
USER appuser

EXPOSE 8000

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
