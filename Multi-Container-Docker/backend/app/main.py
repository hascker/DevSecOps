from fastapi import FastAPI, HTTPException
import psycopg2
import os
import logging
import socket



app = FastAPI()

@app.get("/whoami")
def whoami():
    return {"container": socket.gethostname()}

    
# Basic logging (Phase 2 reliability)
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

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
def health():
    """
    Healthcheck used by Docker.
    App is healthy ONLY if DB is reachable.
    """
    try:
        conn = get_db_connection()
        conn.close()
        return {"status": "healthy"}
    except Exception as e:
        logger.error(f"Healthcheck failed: {e}")
        raise HTTPException(status_code=503, detail="Database not ready")


@app.get("/")
def read_root():
    return {
        "message": (
            "FastAPI running behind Nginx. "
            "Multi-container Docker demo by Omer Mohammed (DevSecOps)."
        )
    }


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
