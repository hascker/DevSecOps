# ▶️ How to Clone and Run the Project

This document explains **step-by-step** how to clone, run, and deploy the project locally or on an AWS EC2 instance.

---

## 📋 Prerequisites

Ensure the following are installed:

- Git
- Docker (v20+)
- Docker Compose (v2+)

Verify installation:
```bash
git --version
docker --version
docker compose version
```

---

## 🖥️ Run Locally

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/omermd529/OmerOps.git
cd Multi-Container-Docker
```

---

### 2️⃣ Start the Application
```bash
docker compose up -d
```

Docker Compose will start:
- FastAPI backend
- PostgreSQL
- Nginx
- Prometheus
- Grafana
- Loki
- Promtail

---

### 3️⃣ Access the Services

| Service | URL |
|------|----|
| Application | http://localhost |
| FastAPI Docs | http://localhost/docs |
| Grafana | http://localhost:3000 |
| Prometheus | http://localhost:9090 |

**Grafana default credentials**
- Username: `admin`
- Password: `admin` (change on first login)

---

### 4️⃣ Stop the Application
```bash
docker compose down
```

---

## ☁️ Run on AWS EC2

### 1️⃣ Launch an EC2 Instance

- AMI: **Amazon Linux 2023**
- Instance type: `t2.micro` or higher
- Configure inbound rules:
  - 22 (SSH)
  - 80 (Application)
  - 3000 (Grafana)

---

### 2️⃣ Connect to EC2
```bash
ssh -i <your-key.pem> ec2-user@<EC2_PUBLIC_IP>
```

---

### 3️⃣ Install Git and Docker
```bash
sudo yum update -y
sudo yum install git docker -y
sudo systemctl start docker
sudo systemctl enable docker
sudo usermod -aG docker ec2-user
newgrp docker
```

---

### 4️⃣ Clone the Repository
```bash
git clone https://github.com/omermd529/OmerOps.git
cd Multi-Container-Docker
```

---

### 5️⃣ Run the Application
```bash
docker compose up -d
```

---

### 6️⃣ Access Services on EC2

| Service | URL |
|------|----|
| Application | http://<EC2_PUBLIC_IP> |
| Grafana | http://<EC2_PUBLIC_IP>:3000 |

---

## 🔁 Updating the Deployment

To pull the latest changes and redeploy manually:

```bash
git pull origin main
docker compose pull
docker compose up -d
```

In normal operation, deployments are handled automatically via GitHub Actions and a self-hosted runner.

---

## 🧑‍💻 Self-Hosted GitHub Runner (Deployment Automation)

This project uses a **self-hosted GitHub Actions runner** installed on the same EC2 instance where the application runs.

### Key Points
- Runner is installed directly on EC2
- Configured as a **system service**
- Starts automatically on instance reboot
- No need to manually run `./run.sh`
- Enables real production-style deployments

### Automated Deployment Flow
```
GitHub Push
   ↓
GitHub Actions Workflow
   ↓
Self-Hosted Runner (EC2)
   ↓
docker compose pull
   ↓
docker compose up -d
```

---

## 🔐 Repository Secrets (GitHub Actions)

Sensitive values required for CI/CD and deployment are stored securely using **GitHub Repository Secrets**.

### Configured Secrets

| Secret Name | Purpose |
|------------|---------|
| `DOCKERHUB_USERNAME` | Docker Hub username used to push images |
| `DOCKERHUB_TOKEN` | Docker Hub access token/password |
| `EC2_HOST` | Public IP or DNS of the EC2 instance |
| `EC2_USER` | SSH username for EC2 (e.g., ec2-user) |
| `EC2_SSH_KEY` | Private SSH key used by GitHub Actions to connect to EC2 |

### Notes
- Secrets are injected into workflows at runtime
- Secrets are **never committed** to the repository
- SSH access is restricted to the self-hosted runner
- The EC2 instance uses an **Elastic IP** to ensure a stable deployment target

---

## 🧹 Reset Grafana (Optional)

If dashboards or alerts do not update due to provisioning behavior:

```bash
docker compose down
docker volume rm multi-container-docker_grafana_data
docker compose up -d
```

Grafana dashboards and alerts are fully reproducible from code.

---

## 🧠 Notes

- Prometheus is intentionally not exposed publicly in production
- Grafana provisioning happens only at startup
- No manual configuration is required after initial setup

---

## ✅ Summary

Clone the repository → Run Docker Compose → Push code to trigger automated deployment.

This project is fully containerized, reproducible, and production-oriented.
