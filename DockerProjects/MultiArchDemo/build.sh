#!/bin/bash

# Multi-architecture Docker build script
DOCKER_USERNAME="omerdevsecops"
IMAGE_NAME="multiarch-demo"
TAG="latest"

echo "Building multi-architecture Docker image..."

# Create and use a new builder instance
docker buildx create --name multiarch-builder --use --bootstrap

# Build for multiple architectures
docker buildx build \
  --platform linux/amd64,linux/arm64,linux/arm/v7 \
  --tag ${DOCKER_USERNAME}/${IMAGE_NAME}:${TAG} \
  --push \
  .

echo "Multi-arch build complete!"
echo "Image: ${DOCKER_USERNAME}/${IMAGE_NAME}:${TAG}"