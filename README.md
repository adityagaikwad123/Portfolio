# Aditya Gaikwad — Portfolio

A responsive Django portfolio showcasing cloud, backend, AI, and cybersecurity work.

## Local development

```bash
python3 -m venv .venv
source .venv/bin/activate
python3 -m pip install -r requirements.txt
python3 manage.py migrate
python3 manage.py runserver
```

Open `http://127.0.0.1:8000/`.

## Deploy free on GitHub Pages

GitHub Pages hosts a static build of this portfolio for free. The build workflow also copies all downloadable certificate PDFs.

1. Push the latest code to the `main` branch.
2. Open **Settings → Pages** in the GitHub repository.
3. Under **Build and deployment**, select **GitHub Actions**.
4. Open the **Actions** tab and run **Deploy portfolio to GitHub Pages**.

The site will be published at `https://adityagaikwad123.github.io/Portfolio/`.

> GitHub Pages does not run a Django server. The Django project remains available for local development; the GitHub workflow creates the static portfolio that Pages publishes.

Replace `your.email@example.com` in `templates/dashboard.html` with your real email before sharing.
