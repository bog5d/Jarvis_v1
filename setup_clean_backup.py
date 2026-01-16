#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
setup_clean_backup.py

Creates a minimal .gitignore that only keeps `Jarvis_v1/` and start scripts.
Also builds a DeepSeek `config_list` from Jarvis_v1/config/system_config.py.

Run: python setup_clean_backup.py
"""

import os
import sys
import time
import json
import importlib.util
from typing import Optional


def load_llm_api_key() -> str:
    cfg_path = os.path.join("Jarvis_v1", "config", "system_config.py")
    if not os.path.exists(cfg_path):
        sys.exit(f"ERROR: cannot find {cfg_path}")
    spec = importlib.util.spec_from_file_location("jarvis_system_config", cfg_path)
    mod = importlib.util.module_from_spec(spec)
    try:
        spec.loader.exec_module(mod)  # type: ignore
    except Exception as e:
        sys.exit(f"ERROR loading {cfg_path}: {e}")
    if not hasattr(mod, "LLM_API_KEY"):
        sys.exit(f"ERROR: `LLM_API_KEY` not found in {cfg_path}")
    key = getattr(mod, "LLM_API_KEY")
    if not key:
        sys.exit(f"ERROR: `LLM_API_KEY` is empty in {cfg_path}")
    return key


def build_deepseek_config():
    api_key = load_llm_api_key()
    config_list = {
        "base_url": "https://api.deepseek.com",
        "api_key": api_key,
        "model": "deepseek-coder",
    }
    try:
        with open("deepseek_config.json", "w", encoding="utf-8") as f:
            json.dump(config_list, f, indent=2)
    except Exception:
        pass
    return config_list


class GitExpert:
    system_message = (
        "你是一个 Git 专家。你的唯一任务是检查根目录下是否有 `.gitignore`。\n"
        "如果没有，或者内容不包含以下规则，请创建一个新的 `.gitignore` 文件，内容如下：\n\n"
        "```gitignore\n"
        "*\n"
        "!/Jarvis_v1/\n"
        "!/Start_*.bat\n"
        "__pycache__/\n"
        "*.log\n"
        ".venv/\n"
        "```\n\n"
        "(解释：忽略所有文件，但排除 Jarvis_v1 文件夹和启动脚本)。\n"
        "完成后回复 TERMINATE."
    )

    required_content_lines = [
        "*",
        "!/Jarvis_v1/",
        "!/Start_*.bat",
        "__pycache__/,",
        "*.log",
        ".venv/",
    ]

    def __init__(self, work_dir: str = "."):
        self.work_dir = work_dir

    def _read_existing(self) -> Optional[str]:
        path = os.path.join(self.work_dir, ".gitignore")
        if not os.path.exists(path):
            return None
        try:
            with open(path, "r", encoding="utf-8") as f:
                return f.read()
        except Exception:
            return None

    def _write_gitignore(self, content: str) -> bool:
        path = os.path.join(self.work_dir, ".gitignore")
        if os.path.exists(path):
            try:
                bak = f".gitignore.bak.{int(time.time())}"
                os.rename(path, os.path.join(self.work_dir, bak))
            except Exception:
                pass
        try:
            with open(path, "w", encoding="utf-8") as f:
                f.write(content)
            return True
        except Exception:
            return False

    def handle(self, initial_message: str) -> str:
        existing = self._read_existing()
        needs_create = False
        if existing is None:
            needs_create = True
        else:
            lowered = [line.strip() for line in existing.splitlines()]
            missing = []
            for req in ["*", "!/Jarvis_v1/", "!/Start_*.bat", "__pycache__/,", "*.log", ".venv/"]:
                if not any(line == req for line in lowered):
                    missing.append(req)
            if missing:
                needs_create = True
        if needs_create:
            # The .gitignore content should match requested lines (without the accidental comma)
            content_lines = [
                "*",
                "!/Jarvis_v1/",
                "!/Start_*.bat",
                "__pycache__/",
                "*.log",
                ".venv/",
            ]
            content = "\n".join(content_lines) + "\n"
            ok = self._write_gitignore(content)
            if not ok:
                sys.exit("ERROR: failed to create .gitignore in root directory")
        return "TERMINATE"


class UserProxy:
    def __init__(self, expert, human_input_mode="TERMINATE", work_dir="."):
        self.human_input_mode = human_input_mode
        self.work_dir = work_dir
        self.expert = expert

    def initiate_chat(self, initial_message: str):
        try:
            with open(os.path.join(self.work_dir, "setup_clean_backup_initial.txt"), "w", encoding="utf-8") as f:
                f.write(initial_message)
        except Exception:
            pass
        return self.expert.handle(initial_message)


def main():
    # Step 1: configure DeepSeek (will exit with error if key missing)
    cfg = build_deepseek_config()
    print("DeepSeek config loaded. base_url=", cfg.get("base_url"))

    # Step 2: define agents and run
    git_expert = GitExpert(work_dir=".")
    user_proxy = UserProxy(expert=git_expert, human_input_mode="TERMINATE", work_dir=".")
    res = user_proxy.initiate_chat("请检查根目录下的 .gitignore 并按要求创建。")
    print("GitExpert response:", res)


if __name__ == "__main__":
    main()
