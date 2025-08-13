# Multi-Architecture Docker Demo 🏗️

> Demonstrates building Docker images for multiple CPU architectures (AMD64, ARM64, ARMv7) using Docker Buildx.

## 🎯 Overview

This project showcases how to build Docker images that run on different CPU architectures, essential for modern cloud deployments and edge computing.

## 🚀 Quick Start

### Prerequisites
- Docker with Buildx enabled
- Docker Hub account (for pushing images)

### Build Multi-Arch Image

```bash
# Make build script executable
chmod +x build.sh

# Run the build (requires Docker Hub login)
./build.sh
```

### Manual Build Commands

```bash
# Create builder instance
docker buildx create --name multiarch-builder --use

# Build for multiple platforms
docker buildx build \
  --platform linux/amd64,linux/arm64,linux/arm/v7 \
  --tag omerdevsecops/multiarch-demo:latest \
  --push \
  .
```

### Test Locally

```bash
# Pull and run the multi-arch image
docker run -p 8080:8080 omerdevsecops/multiarch-demo:latest

# Test endpoint
curl http://localhost:8080

# Build for current platform only (alternative)
docker build -t multiarch-demo .
docker run -p 8080:8080 multiarch-demo
```

## 🏗️ Architecture Support

- **linux/amd64** - Intel/AMD 64-bit
- **linux/arm64** - ARM 64-bit (Apple Silicon, AWS Graviton)
- **linux/arm/v7** - ARM 32-bit (Raspberry Pi)

## 🛠️ Key Features

- Cross-platform compilation with Go
- Multi-stage Docker builds
- Platform-specific build arguments
- Buildx for multi-architecture support

## 📚 Learning Objectives

- ✅ Multi-architecture Docker builds
- ✅ Docker Buildx usage
- ✅ Cross-compilation techniques
- ✅ Platform-specific optimizations