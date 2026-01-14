from fastapi import FastAPI, HTTPException,Request
import psycopg2
import os
import logging
import socket
import json
import uuid

app = FastAPI()

@app.get("/whoami")
def whoami():
    return {"container": socket.gethostname()}


# Basic logging (Phase 2 reliability)
logger = logging.getLogger("app")
logger.setLevel(logging.INFO)

handler = logging.StreamHandler()
formatter = logging.Formatter('%(message)s')
handler.setFormatter(formatter)
logger.handlers = [handler]


DB_HOST = os.getenv("DB_HOST")
DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")


def get_db_connection():
    """
    Create a short-lived DB connection with timeout.
    """
    return psycopg2.connect(
        host=DB_HOST,
        database=DB_NAME,
        user=DB_USER,
        password=DB_PASSWORD,
        connect_timeout=3
    )


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

@app.middleware("http")
async def request_id_middleware(request: Request, call_next):
    request_id = request.headers.get("X-Request-ID", str(uuid.uuid4()))
    request.state.request_id = request_id

    response = await call_next(request)
    response.headers["X-Request-ID"] = request_id

    return response

@app.get("/")
def read_root(request: Request):
    logger.info(json.dumps({
        "level": "INFO",
        "service": "backend",
        "request_id": request.state.request_id,
        "message": "Root endpoint hit"
    }))
    return {"message": "FastAPI running behind Nginx,project by OmerMohammed DevSecOps"}


@app.get("/db")
def check_db():
    """
    Explicit DB check endpoint (debug/demo).
    """
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
