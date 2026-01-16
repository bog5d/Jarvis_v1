import sys
from pathlib import Path

# Add project root to sys.path
current_file = Path(__file__).resolve()
project_root = current_file.parent.parent.parent
if str(project_root) not in sys.path:
    sys.path.append(str(project_root))

from Jarvis_v1.config import system_config
from Jarvis_v1.utils.logger import setup_logger
import json
from typing import List, Dict, Optional

try:
    from openai import OpenAI
except ImportError:
    OpenAI = None

logger = setup_logger("AI_Brain")

def call_ai(prompt):
    """
    Call the AI model with the given prompt.
    """
    if OpenAI is None:
        logger.error("❌ 'openai' library not installed. Please install it using: pip install openai")
        return None

    api_key = getattr(system_config, "LLM_API_KEY", "YOUR_DEEPSEEK_KEY_HERE")
    base_url = getattr(system_config, "LLM_API_BASE", "https://api.deepseek.com")
    model = getattr(system_config, "LLM_MODEL", "deepseek-chat")

    # Safety check for placeholder key
    if "YOUR_DEEPSEEK_KEY_HERE" in api_key:
        logger.warning("⚠️ AI Key is not set in system_config.py. Skipping AI call.")
        return None

    try:
        client = OpenAI(api_key=api_key, base_url=base_url)

        logger.info(f"🧠 Sending request to {model}...")
        response = client.chat.completions.create(
            model=model,
            messages=[
                {"role": "system", "content": load_system_prompt()},
                {"role": "user", "content": prompt},
            ],
            stream=False
        )
        return response.choices[0].message.content
    except Exception as e:
        logger.error(f"❌ AI Call Failed: {e}")
        return None


def load_system_prompt() -> str:
    """Load system prompt text from prompts/system_prompt.md if present, else fallback."""
    try:
        p = project_root / 'Jarvis_v1' / 'prompts' / 'system_prompt.md'
        if p.exists():
            return p.read_text(encoding='utf-8')
    except Exception:
        pass
    # Fallback prompt
    return "You are Jarvis, the user's local personal assistant. Be concise and helpful."


def retrieve_context(query: str, top_k: int = 3) -> List[Dict[str, str]]:
    """Lightweight retrieval from memory.json by simple keyword matching.

    Returns a list of {'name':..., 'snippet':..., 'path':...}
    """
    mem_file = project_root / 'Jarvis_v1' / 'memory.json'
    results: List[Dict[str, str]] = []
    try:
        if not mem_file.exists():
            return results
        data = json.loads(mem_file.read_text(encoding='utf-8'))
        q = query.lower()
        scores = []
        for k, v in data.items():
            # simple scoring: count keyword hits in snippet and name
            text = (v.get('snippet','') + ' ' + v.get('name','')).lower()
            score = sum(1 for tok in q.split() if tok and tok in text)
            if score > 0:
                scores.append((score, v))
        scores.sort(key=lambda x: x[0], reverse=True)
        for s, v in scores[:top_k]:
            results.append({'name': v.get('name',''), 'snippet': v.get('snippet',''), 'path': v.get('path','')})
    except Exception as e:
        logger.warning(f"Failed to retrieve context: {e}")
    return results


def build_context_text(items: List[Dict[str, str]]) -> str:
    if not items:
        return ""
    parts = []
    for it in items:
        name = it.get('name','')
        snippet = it.get('snippet','')
        parts.append(f"[{name}] {snippet}")
    return "\n---\n".join(parts)

if __name__ == "__main__":
    # Test run
    print(call_ai("Hello, are you there?"))
