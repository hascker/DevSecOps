# 🐳 Caddy Custom Docker Build

This folder contains a multi-stage Docker setup to build [Caddy](https://github.com/caddyserver/caddy) from source using your own fork, and optionally serve static content.

---

## 📁 Folder Contents

- `Dockerfile` – Multi-stage Dockerfile that builds Caddy from Go source and produces a minimal Alpine-based image.
- `Caddyfile` – Basic Caddy configuration to serve static files from `/srv`.
- `site/` – Directory containing static content (e.g. `index.html`) served by Caddy.
- `caddy/` – (Optional) Local copy of your Caddy source. You can use `COPY` to build from it, or pull directly from GitHub in the future.

---

## 🚀 Usage

### 🔧 Build Docker Image

Run the following from this folder:

```bash
docker build -t my-caddy .
```

### ▶️ Run the Container

```bash
docker run -d -p 80:80 \
  -v $(pwd)/Caddyfile:/etc/caddy/Caddyfile \
  -v $(pwd)/site:/srv \
  my-caddy
```

### 🌐 Access

Open your browser and visit:

```
http://localhost
```

You should see your static site's `index.html` served by Caddy.

---

## 🛠️ Optional Improvements

- Add plugins using [`xcaddy`](https://github.com/caddyserver/xcaddy)
- Serve a Go API backend (reverse proxy)
- Add HTTPS and TLS settings in the `Caddyfile`
- Use GitHub Actions to automate image builds
- Push built image to Docker Hub or GitHub Container Registry (GHCR)

---

## 🧱 Example Caddyfile

Here’s a simple `Caddyfile` used in this project:

```
:80

root * /srv
file_server
```

This tells Caddy to listen on port 80 and serve files from `/srv`, which is mapped to your local `site/` folder.

---

## 📄 License

This setup is based on [Caddy](https://github.com/caddyserver/caddy), which is licensed under the **Apache 2.0 License**. You can optionally copy the `LICENSE` file into this directory for reference.


