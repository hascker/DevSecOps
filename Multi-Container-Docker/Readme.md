# Multi-Container FastAPI Application (Docker Compose)

This project demonstrates a **production-style, multi-container application** built with **Docker Compose**, showcasing security, reliability, and scalability best practices.

The stack consists of:

* **PostgreSQL** – persistent data layer
* **FastAPI** – application layer
* **Nginx** – reverse proxy and single entry point

The goal of this project is **learning and demonstration**, not just running containers.

---

## Architecture Overview

```
Client
  |
  v
Nginx (port 80)
  |
  v
FastAPI (internal port 8000)
  |
  v
PostgreSQL (internal port 5432)
```

### Key Design Decisions

* Only **Nginx** is exposed to the host
* Backend and database communicate over **Docker’s internal network**
* PostgreSQL data is persisted using a **named Docker volume**
* Containers are **health-aware** and **self-healing**

---

## Repository Structure

```
app/
├── docker-compose.yml
├── backend/
│   ├── Dockerfile
│   ├── requirements.txt
│   └── app/
│       └── main.py
└── nginx/
    └── nginx.conf
```

---

## Features Implemented

### ✅ Multi-Container Architecture

* Each component runs in its own container
* Clean separation of concerns

### ✅ Secure Docker Image

* Multi-stage Docker build
* Runtime container runs as a **non-root user**
* Minimal base image (`python:slim`)

### ✅ Reliability & Self-Healing

* Application and database healthchecks
* Health-based startup ordering
* Automatic restarts using `restart: unless-stopped`

### ✅ Networking Best Practices

* Internal service-to-service communication via Docker DNS
* No hardcoded IPs
* No unnecessary port exposure

---

## Prerequisites

* Docker
* Docker Compose (v2)

---

## How to Run

From the `app/` directory:

```bash
docker compose up --build
```

Once started, access the application at:

```
http://localhost
```

---

## Available Endpoints

| Endpoint  | Description                      |
| --------- | -------------------------------- |
| `/`       | Root endpoint (served via Nginx) |
| `/health` | Application healthcheck          |
| `/db`     | Database connectivity test       |

---

## Health & Reliability

* PostgreSQL health is verified using `pg_isready`
* FastAPI health depends on **successful DB connectivity**
* Nginx starts only after the backend is healthy

You can inspect health status with:

```bash
docker ps
```

---

## Scaling the Backend

FastAPI can be horizontally scaled without configuration changes:

```bash
docker compose up --scale backend=3
```

Docker’s internal DNS automatically load-balances traffic across replicas.

---

## Why This Project Matters

This project is intentionally designed to mirror **real production systems**:

* Reverse proxy pattern
* Service discovery via DNS
* Health-based orchestration
* Secure container runtime

It builds a strong foundation for:

* Kubernetes
* Amazon ECS
* CI/CD pipelines
* DevSecOps practices

---

## Next Steps (Planned)

* CI/CD with GitHub Actions
* Image security scanning
* Observability (structured logs, access logs)
* Cloud deployment (ECS / Kubernetes)

---

## Author

**Omer Mohammed**
DevSecOps / Cloud Engineer

---

## License

This project is for learning and demonstration purposes.
