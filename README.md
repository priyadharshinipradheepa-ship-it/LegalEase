# LegalEase — AI-Powered Legal Document Generator

Complete runnable implementation based on the supplied LegalEase project specification.

## Features

- Streamlit frontend
- FastAPI backend
- Google Gemini document generation
- Inputs: document type, parties, terms, effective date
- Editable generated document
- Styled HTML preview
- TXT, DOCX and PDF downloads
- DOCX logo, headings, terms table and footer
- Branded PDF header/footer
- `.env` configuration
- Docker / Docker Compose
- API and exporter tests

## Run locally

Python 3.10+ recommended.

### Windows

```powershell
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
copy .env.example .env
```

### macOS/Linux

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
```

Put your API key in `.env`:

```env
GEMINI_API_KEY=YOUR_KEY
GEMINI_MODEL=gemini-1.5-pro
BACKEND_URL=http://localhost:8000
```

The source specification selects `gemini-2.5-flash`. If that model is unavailable for your current Gemini account, change `GEMINI_MODEL` to a model available to you.

### Start backend

```bash
uvicorn backend.main:app --reload --port 8000
```

### Start frontend

In a second terminal:

```bash
streamlit run frontend/app.py
```

Open `http://localhost:8501`.

FastAPI docs: `http://localhost:8000/docs`.

### Run tests

```bash
pytest -q
```

### Docker

Create `.env`, then:

```bash
docker compose up --build
```

## Project structure

```text
LegalEase/
├── ai_core/gemini_generator.py
├── assets/logo.png
├── backend/main.py
├── backend/routes.py
├── backend/schemas.py
├── document_utils/exporters.py
├── document_utils/text_utils.py
├── frontend/app.py
├── tests/test_api.py
├── tests/test_exporters.py
├── .env.example
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
└── start.py
```

## Legal-use disclaimer

This is an AI-assisted drafting application, not legal advice. Generated text may be incomplete, inaccurate, or unsuitable for a particular jurisdiction or situation. Have a qualified legal professional review documents before relying on them.

## Branding

Replace `assets/logo.png` with your own PNG logo. DOCX and PDF exports use it automatically.
