# Docker Projects 🐳

> Collection of Docker containerization projects showcasing multi-stage builds, application containerization, and image optimization techniques.

---

## 📁 Projects Overview

| Project | Description | Key Features |
|---------|-------------|--------------|
| **Docker/** | Basic Python web application containerization | Simple Dockerfile, Python Flask app |
| **DockerMultiStageBuild/CaddyCustomBuild/** | Multi-stage Caddy web server build | Multi-stage optimization, custom Caddy build |
| **MultiArchDemo/** | Multi-architecture Docker builds | Cross-platform compilation, Docker Buildx |

---

## 🚀 Quick Start

### Prerequisites
- Docker installed and running
- Basic understanding of containerization concepts

### Running Projects

#### 1. Basic Docker Project
```bash
cd Docker/
docker build -t python-web-app .
docker run -p 5000:5000 python-web-app
```

#### 2. Multi-Stage Caddy Build
```bash
cd DockerMultiStageBuild/CaddyCustomBuild/
docker build -t caddy-custom .
docker run -p 80:80 caddy-custom
```

#### 3. Multi-Architecture Demo
```bash
cd MultiArchDemo/
chmod +x build.sh
./build.sh
```

---

## 🛠️ Technologies Used

- **Docker** - Containerization platform
- **Docker Buildx** - Multi-platform build support
- **Python Flask** - Web application framework
- **Go** - Cross-platform compilation
- **Caddy** - Modern web server with automatic HTTPS
- **Multi-stage builds** - Image size optimization

---

## 📚 Learning Objectives

- ✅ Container image creation and optimization
- ✅ Multi-stage build patterns
- ✅ Multi-architecture builds (AMD64, ARM64, ARMv7)
- ✅ Application containerization best practices
- ✅ Docker security considerations
- ✅ Image size reduction techniques
- ✅ Cross-platform deployment strategies

---

## 🔗 Related Documentation

- [Docker Best Practices](https://docs.docker.com/develop/dev-best-practices/)
- [Multi-stage Builds](https://docs.docker.com/develop/dev-best-practices/dockerfile_best-practices/#use-multi-stage-builds)