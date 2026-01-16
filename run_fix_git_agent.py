#!/usr/bin/env python3
"""
run_fix_git_agent.py

Sets DeepSeek env vars from deepseek_config.json and runs fix_git_agent.py in-process.
"""
import json
import os
import runpy
import sys

CONFIG_PATH = os.path.join(os.getcwd(), "deepseek_config.json")
if not os.path.isfile(CONFIG_PATH):
    print(f"ERROR: missing {CONFIG_PATH}")
    sys.exit(1)

with open(CONFIG_PATH, "r", encoding="utf-8") as f:
    cfg = json.load(f)

api_key = cfg.get("api_key")
base_url = cfg.get("base_url")
if not api_key or not base_url:
    print("ERROR: deepseek_config.json must contain 'api_key' and 'base_url'")
    sys.exit(1)

os.environ["OPENAI_API_KEY"] = api_key
os.environ["OPENAI_API_BASE"] = base_url
os.environ["USE_AUTOGEN"] = "1"

print("Running fix_git_agent.py with DeepSeek key and base:")
print(f"OPENAI_API_BASE={os.environ.get('OPENAI_API_BASE')}")

try:
    runpy.run_path("fix_git_agent.py", run_name="__main__")
except SystemExit as e:
    # propagate exit code
    code = int(e.code) if isinstance(e.code, int) else 1
    sys.exit(code)
except Exception as e:
    print("ERROR: exception while running fix_git_agent.py:", e)
    raise
