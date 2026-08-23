from pathlib import Path
from shutil import copytree, rmtree


ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "_site"
template = (ROOT / "templates" / "dashboard.html").read_text(encoding="utf-8")

template = template.replace("{% load static %}\n", "")
for certificate in (
    "gemini-certificate.pdf",
    "deloitte-cyber.pdf",
    "deloitte-technology.pdf",
    "oci-generative-ai-professional.pdf",
    "tcs-cybersecurity.pdf",
):
    template = template.replace(
        "{% static 'certificates/" + certificate + "' %}",
        "static/certificates/" + certificate,
    )

if OUTPUT.exists():
    rmtree(OUTPUT)
OUTPUT.mkdir()
(OUTPUT / "index.html").write_text(template, encoding="utf-8")
copytree(ROOT / "static", OUTPUT / "static")
