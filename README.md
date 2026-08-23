# Aditya Gaikwad — Portfolio

## Run locally

```bash
python3 manage.py runserver
```

Open `http://127.0.0.1:8000/`.

## Publish on GitHub Pages

1. Create a GitHub repository and push this project to its `main` branch.
2. In the repository, open **Settings → Pages** and select **GitHub Actions** as the source.
3. Push to `main` (or run **Deploy portfolio to GitHub Pages** from the Actions tab).

The workflow publishes the self-contained portfolio page automatically. Before sharing it, replace `your.email@example.com` in `templates/dashboard.html` with your real email address.
