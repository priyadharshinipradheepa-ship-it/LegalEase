import subprocess
import sys

backend = subprocess.Popen([
    sys.executable, "-m", "uvicorn", "backend.main:app",
    "--host", "127.0.0.1", "--port", "8000"
])
try:
    subprocess.run([sys.executable, "-m", "streamlit", "run", "frontend/app.py", "--server.port", "8501"])
finally:
    backend.terminate()
