# 🐳 Caddy Custom Build with Docker Multi-Stage

[![Built with Docker Multi-Stage](https://img.shields.io/badge/Built%20With-Docker%20Multi--Stage-blue?logo=docker&logoColor=white)](https://docs.docker.com/build/building/multi-stage/)
[![Go](https://img.shields.io/badge/Powered%20by-Go-00ADD8?logo=go&logoColor=white)](https://go.dev)
[![DevSecOps Ready](https://img.shields.io/badge/DevSecOps-Ready-brightgreen?logo=security&logoColor=white)](https://en.wikipedia.org/wiki/DevSecOps)
[![Image Size](https://img.shields.io/badge/Image%20Size-72.5MB-blueviolet)](#)
[![CI/CD Ready](https://img.shields.io/badge/CI%2FCD-Compatible-yellow?logo=githubactions&logoColor=white)](#)

---

## 📦 Overview

This project demonstrates how to build and run the **Caddy web server** using a **Docker multi-stage build** approach to drastically reduce the final image size and improve container performance.

It includes:

- A production-ready `Dockerfile` using multi-stage builds
- A static `Caddyfile` to serve files from a `site/` folder
- A `Dockerfile.single-stage` for comparison

---

## 🏗️ Project Structure

```bash
CaddyCustomBuild/
├── caddy/                # Caddy source code (copied from fork)
├── Caddyfile             # Caddy server configuration
├── site/                 # Static files served by Caddy
├── Dockerfile            # Multi-stage Docker build
├── Dockerfile.single-stage # Single-stage Dockerfile for comparison
└── README.md
```

---

## 🆚 Single-Stage vs Multi-Stage Docker Builds

As part of this project, I experimented with both **single-stage** and **multi-stage** Dockerfiles to build the Caddy server from source using Go.

| Feature                      | Single-Stage Build                    | Multi-Stage Build                     |
|------------------------------|----------------------------------------|----------------------------------------|
| **Image Tag**                | `my-caddy-single-stage`               | `my-caddy`                             |
| **Image Size**               | ❌ `1.2 GB`                            | ✅ `72.5 MB`                            |
| **Includes Go toolchain?**   | ✅ Yes (not needed at runtime)         | ❌ No (only final binary)              |
| **Build Caching**            | ❌ Less efficient                      | ✅ Efficient separation of concerns    |
| **Security Surface**         | ❌ Larger                              | ✅ Smaller, minimal final image        |
| **Prod Readiness**           | ❌ Not recommended                     | ✅ Yes                                  |

### ⚙️ Observations

- The **single-stage build** includes all development tools, source files, and compilers, inflating the final image to **1.2 GB**.
- The **multi-stage build** strips away everything except the `caddy` binary and necessary configs/static files, resulting in a lean **72.5 MB** image.
- This dramatic size reduction is made possible through the **powerful combination of Go and Docker multi-stage builds**.

---

## 🧠 Learnings & Key Takeaways

- Learned to work with multi-stage Docker builds to reduce image bloat.
- Understood the structure of a Go project compiled from source in containers.
- Gained hands-on experience with lightweight Alpine-based builds.
- Built confidence in isolating dev tools from runtime environments.
- Applied `.dockerignore` and `.gitignore` to keep the image lean.
- Practiced working with local volumes and testing containerized static servers.

---

## ▶️ Usage

### 🛠 Build multi-stage image

```bash
docker build -t my-caddy .
```

### 🛠 Build single-stage image

```bash
docker build -f Dockerfile.single-stage -t my-caddy-single-stage .
```

### ▶️ Run container (multi-stage image)

```bash
docker run -d -p 8080:80 \
  -v $(pwd)/site:/srv \
  my-caddy
```

Access at: [http://localhost:8080](http://localhost:8080)

---

## 📬 Contact

If you'd like to connect professionally or are a recruiter looking for a skilled DevOps/Cloud Engineer, feel free to reach out:

- **LinkedIn:** [linkedin.com/in/mdomer529](https://linkedin.com/in/mdomer529)
- **Email:** omermd529@gmail.com
- **Phone:** +91-9032448366

I’m actively open to remote **DevOps** or **DevSecOps** opportunities with a focus on:
**Docker**, **AWS**, **Azure**, **CI/CD**, **Terraform**, **security practices**, and **infrastructure automation**.

---

