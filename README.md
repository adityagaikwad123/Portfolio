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

## Deploy Django on Render

This repository includes `render.yaml` for a production Django deployment.

1. Push the latest code to GitHub.
2. Create a free [Render](https://render.com) account and connect GitHub.
3. Select **New → Blueprint** and choose this repository.
4. Confirm the `aditya-portfolio` service and click **Apply**.
5. Render will install dependencies, collect static files, run migrations, and publish the site at an `.onrender.com` URL.

Every push to `main` automatically redeploys the portfolio. Free Render services spin down after inactivity and wake on the next visit.

## Production notes

- Set `SECRET_KEY` in the host environment; Render generates it from `render.yaml`.
- Add your own domain to `ALLOWED_HOSTS` if you connect one.
- Replace `your.email@example.com` in `templates/dashboard.html` with your real email before sharing.
