# 🐳 Caddy Custom Docker Build

This folder contains a multi-stage Docker setup to build [Caddy](https://github.com/caddyserver/caddy) from source using your own fork, and optionally serve static content.

---

## 📁 Folder Contents

- `Dockerfile` – Multi-stage Dockerfile that builds Caddy from Go source and produces a minimal Alpine-based image.
- `Caddyfile` – Basic Caddy configuration to serve static files from `/srv`.
- `site/` – Directory containing static content (e.g. `index.html`) served by Caddy.
- `caddy/` – Local copy of Caddy source, used to build the custom image.

---

## 🚀 Usage

### 🔧 Build Docker Image

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

Here's a simple `Caddyfile` used in this project:

```
:80

root * /srv
file_server
```

This tells Caddy to listen on port 80 and serve files from `/srv`, which is mapped to your local `site/` folder.

---

## 🧠 Learnings & Key Takeaways

### 🛠️ Technical Skills Practiced
- ✅ Built a Docker **multi-stage image** from source using Go (Golang)
- ✅ Learned how to use `Dockerfile` efficiently to separate build and runtime stages
- ✅ Integrated a real-world open-source project (Caddy) into a custom build process
- ✅ Used `alpine` and `scratch` images for lightweight final containers
- ✅ Served static files using Caddy and a minimal configuration (`Caddyfile`)
- ✅ Gained experience troubleshooting **Git submodules**, **symlinks**, and `.git` folders
- ✅ Used `rm -rf`, `cp -R`, and Git commands to clean and refactor repo structure

### 🔁 Git & GitHub Workflow
- ✅ Forked and cloned a real project (Caddy)
- ✅ Used `git remote`, `git add`, `git rm`, and `git push` with SSH authentication
- ✅ Handled submodule errors by removing `.git` internals
- ✅ Created a separate branch (`add-caddy-multistage`) for clean commits and PR tracking

### 📦 DevOps Principles Applied
- Emphasis on **clean build pipelines** and separating build context from runtime
- Leveraged **small base images** and minimal dependencies
- Practiced **layer caching** and optimization for faster Docker builds

### 📉 Lightweight Final Image
With the powerful combination of **Golang and Docker multi-stage builds**, the final container image size was only **72.5 MB** — demonstrating best practices in image optimization.

---

🚀 This project helped me deepen my understanding of real-world Docker image construction, multi-stage builds, and source-code-based containerization. It also improved my confidence working with Git, submodules, and project structure cleanup.

---

## 📄 License

This setup is based on [Caddy](https://github.com/caddyserver/caddy), which is licensed under the **Apache 2.0 License**. 

## 📬 Contact

If you'd like to connect professionally or are a recruiter looking for a skilled DevOps/Cloud Engineer, feel free to reach out:

- **LinkedIn:** [linkedin.com/in/mdomer529](https://linkedin.com/in/mdomer529)
- **Email:** omermd529@gmail.com
- **Phone:** +91-9032448366

I’m actively open to remote **DevOps** or **DevSecOps** opportunities with a focus on:
**Docker**, **AWS**, **Azure**, **CI/CD**, **Terraform**, **security practices**, and **infrastructure automation**.
