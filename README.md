# 🚀 OmerOps – DevSecOps Portfolio

A unified portfolio of production-ready implementations by **Omer Mohammed**. This repository showcases real-world applications of DevSecOps principles: shifting security left, automating infrastructure, and optimizing containerized environments.

---

## ⭐ Featured: Production-Grade Multi-Container System
**Location:** [`/Multi-Container-Docker`](./Multi-Container-Docker)

This is a deep-dive into high-availability container orchestration. It moves beyond basic tutorials to address real-world production concerns:

* **Security-First Builds:** Multi-stage Dockerfiles reducing attack surface by 65%.
* **Vulnerability Management:** Automated **Trivy** scanning and **Gitleaks** secret detection.
* **Runtime Hardening:** Implementation of non-root users, health checks, and resource limits.
* **CI/CD Integration:** Automated deployment workflows to AWS EC2 via GitHub Actions.

---

## 📂 Active Workstreams

| Project Category | Focus Area | Tech Stack |
| :--- | :--- | :--- |
| **DevSecOps Projects** | [Harness CI/CD](./DevSecOps-Projects/Harness-Demo-CI-CD) | GitLab CI, Flask, Gitleaks, AWS |
| **Containerization** | [Hardened Docker Builds](./Multi-Container-Docker) | Python, Go, Docker, Multi-stage |
| **Automation** | [Bash Projects](./Automation-Scripting/BashProjects) | Shell Scripting, Linux Automation |

---

## 🛠️ Tech Stack & Security Tooling

* **Cloud:** AWS (EC2, IAM, S3, CloudWatch)
* **Containers:** Docker, Docker Compose (Advanced)
* **CI/CD:** GitHub Actions, GitLab CI/CD
* **Security (SAST/SCA):** Trivy, Gitleaks, Checkov
* **Languages:** Python (Primary), Bash, Golang (Foundational)

---

## 🛡️ Security Implementation
Every project in this repository follows a **Security-by-Design** approach:
1.  **Secret Management:** No hardcoded secrets; validated via Gitleaks.
2.  **Image Scanning:** All images are scanned for CVEs before deployment.
3.  **Least Privilege:** IAM roles and container users are restricted to the minimum permissions required.

---

## 📌 About
This portfolio reflects my journey in engineering resilient cloud infrastructure. It aligns with my professional focus on AWS and DevSecOps best practices.

* **LinkedIn:** [Your LinkedIn Profile Link]
* **Status:** Actively maintaining and adding modular Terraform/IaC components.

---

### 🚀 Recent Activity
- ✅ Optimized Multi-Container image sizes.
- ✅ Integrated Gitleaks into local pre-commit hooks.
- ✅ Documented production-ready deployment to EC2.