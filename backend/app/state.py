"""Runtime-switchable LLM settings (changeable live from the UI, no restart).

Seeded from .env at startup; the /api/model endpoint mutates the model.
Supports Google Gemini (Free) and OpenAI.
"""
from . import config

GEMINI_MODELS = [
    {"id": "gemini-2.0-flash", "label": "Gemini 2.0 Flash (Free, Recommended)"},
    {"id": "gemini-1.5-flash", "label": "Gemini 1.5 Flash (Free, Fast)"},
    {"id": "gemini-1.5-pro", "label": "Gemini 1.5 Pro (Free, Advanced)"},
]

OPENAI_MODELS = [
    {"id": "gpt-4o-mini", "label": "gpt-4o-mini (Fast & Budget)"},
    {"id": "gpt-4o", "label": "gpt-4o (Higher Quality)"},
    {"id": "gpt-5.1", "label": "gpt-5.1"},
]

_state = {
    "provider": config.DEFAULT_PROVIDER,
    "model": config.DEFAULT_MODEL,
}


def provider() -> str:
    return _state["provider"]


def current_model() -> str:
    return _state["model"]


def options() -> dict:
    return {
        "provider": provider(),
        "current_model": current_model(),
        "gemini_models": GEMINI_MODELS,
        "openai_models": OPENAI_MODELS,
    }


def set_model(model_id: str) -> dict:
    all_models = {m["id"]: "gemini" for m in GEMINI_MODELS}
    all_models.update({m["id"]: "openai" for m in OPENAI_MODELS})
    if model_id in all_models:
        _state["model"] = model_id
        _state["provider"] = all_models[model_id]
        return {"ok": True, "provider": _state["provider"], "current_model": current_model()}
    return {"ok": False, "error": f"unknown model {model_id}"}
