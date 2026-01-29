# 🚀 Production-Style Multi-Container DevSecOps Project

This project demonstrates a **production-style containerized backend platform** built using **FastAPI, Docker, Nginx, PostgreSQL**, with **security scanning, observability, CI/CD, alerting, and cloud deployment** on AWS EC2.

The goal is to showcase **real-world DevSecOps and SRE practices**, not just running containers locally.

---

## 🧱 Architecture Overview

### Application Request Flow

Client → Nginx → FastAPI → PostgreSQL

### Observability & CI/CD (Parallel)

Logs → Promtail → Loki → Grafana  
Metrics → Prometheus → Grafana  
CI → GitHub Actions  
CD → Self-hosted GitHub Runner (EC2)  
Security → Trivy  

---

## 🖼️ Architecture Diagram

Multi-Container-Docker/ArchImage.png

---

## 🧩 Tech Stack

### Application Layer
- FastAPI
- PostgreSQL 15
- Nginx
- Docker & Docker Compose

### Observability
- Prometheus
- Grafana
- Loki
- Promtail

### DevSecOps
- GitHub Actions (CI/CD)
- Trivy (Security scanning)
- Self-hosted GitHub Runner
- AWS EC2 (Amazon Linux)

---

## 🔐 Security Practices

- Multi-stage Docker builds
- Non-root containers
- Trivy vulnerability scanning
- CI fails on HIGH / CRITICAL findings
- Secrets stored in GitHub Secrets

---

## 📊 Observability

### Logging
Container Logs → Promtail → Loki → Grafana

### Metrics
FastAPI exposes /metrics  
Prometheus scrapes backend:8000/metrics

---

## 📈 Grafana Dashboards

- Request rate
- Error rate (4xx / 5xx)
- Latency (P50 / P95 / P99)
- Service availability

---

## 🚨 Alerts (Grafana)

### Service Down
- up{job="fastapi"} == 0
- Pending: 5 minutes

### High Error Rate
- 5xx error rate over rolling window

---

## ⚙️ CI Pipeline

1. Build Docker image
2. Push to Docker Hub
3. Scan with Trivy
4. Fail on vulnerabilities

---

## 🚀 CD Pipeline

GitHub → Self-hosted runner → docker compose pull → docker compose up -d

---

## ☁️ Cloud Deployment

- AWS EC2
- Amazon Linux 2023
- Docker Compose runtime

---

## 🧠 Key Learnings

- Production-grade Docker networking
- Centralized logs & metrics
- CI security gates
- Self-hosted GitHub runners
- Grafana alerting (SLO-based)

---

## 🔜 Future Enhancements

- Alertmanager
- Terraform
- Kubernetes (EKS)

---

## 👨‍💻 Author

Mohammed Omer  
DevOps / Cloud Engineer
