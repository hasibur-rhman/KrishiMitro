import os
from pathlib import Path
from dotenv import load_dotenv

BASE_DIR = Path(__file__).resolve().parent.parent  # backend/
load_dotenv(BASE_DIR.parent / ".env")
load_dotenv(BASE_DIR / ".env")

# LLM Providers: Gemini (Free) or OpenAI
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY", "")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "")

# Auto-detect default provider: prefer Gemini if GEMINI_API_KEY is present or key starts with AIzaSy
_active_key = GEMINI_API_KEY or OPENAI_API_KEY
if GEMINI_API_KEY or _active_key.startswith("AIzaSy"):
    DEFAULT_PROVIDER = "gemini"
    DEFAULT_MODEL = os.getenv("GEMINI_MODEL", "gemini-2.0-flash")
else:
    DEFAULT_PROVIDER = os.getenv("LLM_PROVIDER", "gemini")
    DEFAULT_MODEL = os.getenv("GEMINI_MODEL", "gemini-2.0-flash") if DEFAULT_PROVIDER == "gemini" else os.getenv("OPENAI_MODEL", "gpt-4o-mini")

GEMINI_MODEL = os.getenv("GEMINI_MODEL", "gemini-2.0-flash")
OPENAI_MODEL = os.getenv("OPENAI_MODEL", "gpt-4o-mini")
GEMINI_BASE_URL = "https://generativelanguage.googleapis.com/v1beta/openai/"
OPENAI_BASE_URL = os.getenv("OPENAI_BASE_URL", None)

# bdapps TAP API — set these to switch from simulation to the real sandbox
BDAPPS_APP_ID = os.getenv("BDAPPS_APP_ID", "")
BDAPPS_PASSWORD = os.getenv("BDAPPS_PASSWORD", "")
BDAPPS_BASE_URL = os.getenv("BDAPPS_BASE_URL", "https://developer.bdapps.com")

DATA_DIR = BASE_DIR / "data"
KB_DIR = DATA_DIR / "kb"
CHROMA_DIR = str(BASE_DIR / ".chroma")
DB_PATH = str(BASE_DIR / "agrisense.sqlite3")

MAX_AGENT_ITERATIONS = 10
