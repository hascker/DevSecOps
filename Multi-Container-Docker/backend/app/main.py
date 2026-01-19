from fastapi import FastAPI, HTTPException, Request
import psycopg2
import os
import logging
import socket
import json
import uuid
import time

from prometheus_client import Counter, Histogram, generate_latest
from starlette.responses import Response

app = FastAPI(title="Multi-Container FastAPI App")

# -------------------------------------------------------------------
# Prometheus Metrics
# -------------------------------------------------------------------

REQUEST_COUNT = Counter(
    "http_requests_total",
    "Total HTTP requests",
    ["method", "endpoint", "status"]
)

REQUEST_LATENCY = Histogram(
    "http_request_duration_seconds",
    "HTTP request latency",
    ["endpoint"]
)

# -------------------------------------------------------------------
# Logging Setup (JSON logs for Loki)
# -------------------------------------------------------------------

logger = logging.getLogger("backend")
logger.setLevel(logging.INFO)

handler = logging.StreamHandler()
formatter = logging.Formatter("%(message)s")
handler.setFormatter(formatter)
logger.handlers = [handler]

# -------------------------------------------------------------------
# Environment Variables
# -------------------------------------------------------------------

DB_HOST = os.getenv("DB_HOST")
DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")

# -------------------------------------------------------------------
# Database Connection
# -------------------------------------------------------------------

def get_db_connection():
    return psycopg2.connect(
        host=DB_HOST,
        database=DB_NAME,
        user=DB_USER,
        password=DB_PASSWORD,
        connect_timeout=3
    )

# -------------------------------------------------------------------
# Middleware: Request ID
# -------------------------------------------------------------------

@app.middleware("http")
async def request_id_middleware(request: Request, call_next):
    request_id = request.headers.get("X-Request-ID", str(uuid.uuid4()))
    request.state.request_id = request_id

    response = await call_next(request)
    response.headers["X-Request-ID"] = request_id
    return response

# -------------------------------------------------------------------
# Middleware: Prometheus Metrics
# -------------------------------------------------------------------

@app.middleware("http")
async def prometheus_middleware(request: Request, call_next):
    # Do NOT record metrics for Prometheus scrape endpoint
    if request.url.path == "/metrics":
        return await call_next(request)

    start_time = time.time()
    response = await call_next(request)
    latency = time.time() - start_time

    REQUEST_COUNT.labels(
        method=request.method,
        endpoint=request.url.path,
        status=response.status_code
    ).inc()

    REQUEST_LATENCY.labels(
        endpoint=request.url.path
    ).observe(latency)

    return response

# -------------------------------------------------------------------
# Routes
# -------------------------------------------------------------------

@app.get("/")
def root(request: Request):
    logger.info(json.dumps({
        "level": "INFO",
        "service": "backend",
        "request_id": request.state.request_id,
        "message": "Root endpoint hit"
    }))
    return {
        "message": "FastAPI running behind Nginx",
        "project": "Multi-Container DevSecOps by Omer Mohammed"
    }

@app.get("/whoami")
def whoami():
    return {"container": socket.gethostname()}

@app.get("/health")
def health(request: Request):
    try:
        conn = get_db_connection()
        conn.close()

        logger.info(json.dumps({
            "level": "INFO",
            "service": "backend",
            "request_id": request.state.request_id,
            "message": "Healthcheck passed"
        }))

        return {"status": "healthy"}

    except Exception as e:
        logger.error(json.dumps({
            "level": "ERROR",
            "service": "backend",
            "request_id": request.state.request_id,
            "error": str(e)
        }))
        raise HTTPException(status_code=503, detail="Database not ready")

@app.get("/db")
def check_db():
    try:
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute("SELECT 1;")
        result = cur.fetchone()
        cur.close()
        conn.close()
        return {"db_status": result[0]}
    except Exception as e:
        logger.error(f"Database query failed: {e}")
        raise HTTPException(status_code=500, detail="Database error")

@app.get("/metrics")
def metrics():
    return Response(generate_latest(), media_type="text/plain")
