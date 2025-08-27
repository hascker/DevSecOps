# harness-demo

A simple Flask web application that displays an animated rocket with the message "Get Ship Done" - perfect for demonstrating CI/CD pipelines with Harness.

## Features

- Flask web server serving a single-page application
- Animated CSS rocket animation
- Containerized with Docker
- Kubernetes deployment manifests included

## Quick Start

### Local Development

1. Install dependencies:
```bash
cd deploy
pip install -r requirements.txt
```

2. Run the application:
```bash
python app.py
```

3. Open http://localhost:5000 in your browser

### Docker

Build and run with Docker:
```bash
docker build -t harness-demo .
docker run -p 5000:5000 harness-demo
```

### Kubernetes Deployment

Deploy to Kubernetes cluster:
```bash
kubectl apply -f manifest.yaml
```

## Project Structure

```
harness-demo/
├── deploy/
│   ├── app.py              # Flask application
│   ├── requirements.txt    # Python dependencies
│   ├── test_app.py        # Tests
│   ├── static/
│   │   └── style.css      # CSS animations
│   └── templates/
│       └── complete.html  # HTML template
├── Dockerfile             # Container configuration
├── manifest.yaml          # Kubernetes deployment
└── README.md
```

## Technology Stack

- **Backend**: Flask 2.0.2
- **Frontend**: HTML5, CSS3 animations
- **Container**: Docker with Python 3.8 Alpine
- **Orchestration**: Kubernetes