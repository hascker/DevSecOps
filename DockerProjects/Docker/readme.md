# 📦 My First Docker Project

![Docker](https://img.shields.io/badge/Built%20With-Docker-blue?logo=docker)
![FastAPI](https://img.shields.io/badge/API-FastAPI-green?logo=fastapi)
![Deployment](https://img.shields.io/badge/Deployed%20On-AWS%20EC2-orange?logo=amazon-aws)

---

## 🚀 Background

As part of my journey to learn Docker, I created this project to gain hands-on experience with writing Dockerfiles and containerizing Python applications. The code for the application was generated using AI, and my primary focus was on learning how to containerize and deploy it effectively. This sentiment analysis app marks my first successful Docker deployment.

---

## 🧱 Project Structure

This is a simple web application that analyzes the **sentiment of text input** using:

- **FastAPI** – for building the REST API
- **TextBlob** – for basic NLP and sentiment analysis
- **Uvicorn** – ASGI server to run the app

### 📂 Files Included

| File/Folder       | Description                                  |
|-------------------|----------------------------------------------|
| `main.py`         | Core Python script for the FastAPI app       |
| `requirements.txt`| Python dependencies                          |
| `Dockerfile`      | Docker instructions to containerize the app  |

The app was deployed on an **AWS EC2 instance**, and access was opened for port **8000** to allow public testing from my IP.

---

## 🧠 Key Learnings

This project provided several valuable lessons on working with Docker:

- ❌ Initially named the file `Docker` instead of `Dockerfile`, which caused build errors.
- ❌ Missed specifying the destination path in the `COPY` instruction — I learned that Docker's `COPY` requires both source and destination.
- ❌ A subtle typo (`--nocache-dir`) in the pip install command caused failures. I corrected it to `--no-cache-dir`.

These small missteps helped me appreciate the **attention to detail required in DevOps**, and strengthened my debugging and troubleshooting skills.

---

## ✅ What's Next?

Now that I’ve successfully completed this project, I’m looking to explore:

- ✅ Multi-stage builds for smaller, production-ready images
- ✅ Docker Compose for multi-container orchestration
- ✅ Hosting Docker images on Docker Hub
- ✅ CI/CD pipelines using GitHub Actions

---

## 👋 Let’s Connect

If you're a recruiter or engineer reviewing this, I’d love to hear your feedback or suggestions. Feel free to connect with me on [LinkedIn](https://www.linkedin.com/in/mdomer529) or check out more of my work on GitHub.





