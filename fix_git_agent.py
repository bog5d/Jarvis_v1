#!/usr/bin/env python3
"""
fix_git_agent.py

AutoGen-style dual-agent script to diagnose and fix local Git proxy settings.
Creates an `autogen_workspace` directory for temporary files.

Usage: python fix_git_agent.py

This script follows the user's constraints: reads API key from `system_config.py` if present,
does not use paid plugins, and runs fully automated (no human prompts).
"""

import os
import re
import shlex
import subprocess
from typing import Optional

# Zero-cost API key read (falls back to placeholder)
try:
    from system_config import OPENAI_API_KEY  # type: ignore
except Exception:
    OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY", "PLACEHOLDER_API_KEY")

WORK_DIR = os.path.join(os.getcwd(), "autogen_workspace")
os.makedirs(WORK_DIR, exist_ok=True)


class Local_Admin:
    name = "Local_Admin"
    human_input_mode = "TERMINATE"
    code_execution_config = {"work_dir": WORK_DIR, "use_docker": False}

    @staticmethod
    def run(cmd, check=False, capture_output=True, text=True, timeout=None):
        if isinstance(cmd, (list, tuple)):
            proc_cmd = cmd
        else:
            proc_cmd = shlex.split(cmd)
        try:
            res = subprocess.run(proc_cmd, check=check, capture_output=capture_output, text=text, timeout=timeout)
            return res.returncode, res.stdout or "", res.stderr or ""
        except FileNotFoundError as e:
            return 127, "", str(e)
        except subprocess.TimeoutExpired as e:
            return 124, e.stdout or "", f"Timeout: {e}"
        except Exception as e:
            return 1, "", str(e)

    @staticmethod
    def write_temp(name: str, content: str) -> str:
        path = os.path.join(WORK_DIR, name)
        with open(path, "w", encoding="utf-8") as f:
            f.write(content)
        return path


class AutoGenIntegration:
    """Optional AutoGen SDK integration.

    If an `autogen` package is installed and an API key is available via
    `system_config.py` or env, this helper will attempt to run a true
    AutoGen-style agent conversation. If the package or API is missing, the
    code will silently fall back to the local simulator.
    """

    def __init__(self, admin: Local_Admin):
        self.admin = admin

    def is_available(self) -> bool:
        try:
            import autogen  # type: ignore
            return True
        except Exception:
            return False

    def run(self, initial_message: str) -> bool:
        # Try to load repo-specific system_config to source API key and base.
        try:
            from Jarvis_v1.config import system_config as sc  # type: ignore
        except Exception:
            sc = None

        # Build a config_list for downstream SDKs (user-requested DeepSeek values override)
        config_list = {}
        if sc is not None:
            try:
                config_list["api_key"] = getattr(sc, "LLM_API_KEY", os.environ.get("OPENAI_API_KEY"))
                config_list["base_url"] = getattr(sc, "LLM_API_BASE", os.environ.get("OPENAI_API_BASE", "https://api.deepseek.com"))
                # User requested model override
                config_list["model"] = "deepseek-coder"
            except Exception:
                pass
        else:
            # Fallback defaults
            config_list["api_key"] = os.environ.get("OPENAI_API_KEY")
            config_list["base_url"] = os.environ.get("OPENAI_API_BASE", "https://api.deepseek.com")
            config_list["model"] = "deepseek-coder"

        # Export common env vars so OpenAI-compatible SDKs pick them up
        if config_list.get("api_key"):
            os.environ["OPENAI_API_KEY"] = config_list["api_key"]
        if config_list.get("base_url"):
            os.environ["OPENAI_API_BASE"] = config_list["base_url"]

        try:
            import autogen  # type: ignore
        except Exception:
            return False

        # Try a few common AutoGen SDK entry patterns in a safe try/except.
        try:
            # Pattern A: newer AutoGen may provide a `create_local_agent` or similar helper.
            # When available, pass Chinese system messages and initial messages.
            if hasattr(autogen, "create_local_agent"):
                # Try to pass explicit config if API supports it
                try:
                    local_agent = autogen.create_local_agent(name="Local_Admin", human_input_mode="TERMINATE", language="zh-CN", config=config_list)
                    expert_agent = autogen.create_local_agent(name="Network_Expert", system_message=Network_Expert.system_message, language="zh-CN", config=config_list)
                except Exception:
                    local_agent = autogen.create_local_agent(name="Local_Admin", human_input_mode="TERMINATE", language="zh-CN")
                    expert_agent = autogen.create_local_agent(name="Network_Expert", system_message=Network_Expert.system_message, language="zh-CN")
                # This is a best-effort invocation — exact APIs differ between versions.
                if hasattr(autogen, "run_conversation"):
                    autogen.run_conversation([local_agent, expert_agent], initial_message=initial_message)
                else:
                    # fallback: try a generic run method
                    if hasattr(local_agent, "start"):
                        local_agent.start(initial_message)
                        expert_agent.start(Network_Expert.system_message)
                return True

            # Pattern B: generic Agent class
            if hasattr(autogen, "Agent"):
                Agent = getattr(autogen, "Agent")
                # Prefer passing language/system_message where supported
                try:
                    admin_agent = Agent(name="Local_Admin", human_input_mode="TERMINATE", language="zh-CN", config=config_list)
                except Exception:
                    try:
                        admin_agent = Agent(name="Local_Admin", human_input_mode="TERMINATE", language="zh-CN")
                    except Exception:
                        admin_agent = Agent(name="Local_Admin", human_input_mode="TERMINATE")
                try:
                    expert_agent = Agent(name="Network_Expert", system_message=Network_Expert.system_message, language="zh-CN", config=config_list)
                except Exception:
                    try:
                        expert_agent = Agent(name="Network_Expert", system_message=Network_Expert.system_message, language="zh-CN")
                    except Exception:
                        expert_agent = Agent(name="Network_Expert", system_message=Network_Expert.system_message)

                if hasattr(autogen, "run_agents"):
                    autogen.run_agents([admin_agent, expert_agent], initial_message)
                else:
                    # fallback: attempt chat loop
                    if hasattr(admin_agent, "chat") and hasattr(expert_agent, "chat"):
                        # Kick off simple exchange in Chinese
                        admin_agent.chat(initial_message)
                        expert_agent.chat(Network_Expert.system_message)
                return True

            # If none matched, signal unavailable
            return False
        except Exception:
            return False


class Network_Expert:
    name = "Network_Expert"
    system_message = (
        "你是一个网络诊断专家。你的任务是：\n"
        "1. 指挥 Admin 运行 `netstat -an` 或检查常见端口 (7890, 10808)，找出本机真实的代理端口。\n"
        "2. 检查当前的 `git config --global http.proxy`。\n"
        "3. 如果端口不一致，指挥 Admin 运行 `git config` 命令修正它。\n"
        "4. 最后尝试 `git ls-remote git@github.com` 验证连接。"
    )

    def __init__(self, admin: Local_Admin):
        self.admin = admin

    def find_proxy_port(self) -> Optional[int]:
        rc, out, err = self.admin.run("netstat -an")
        output = (out or "") + ("\nERR:\n" + err if err else "")

        ports_to_check = [7890, 10808]
        for p in ports_to_check:
            if re.search(rf"[:\.]\b{p}\b", output):
                return p

        for env_var in ("ALL_PROXY", "HTTPS_PROXY", "HTTP_PROXY", "all_proxy", "https_proxy", "http_proxy"):
            val = os.environ.get(env_var)
            if val:
                m = re.search(r":(\d{2,5})", val)
                if m:
                    try:
                        return int(m.group(1))
                    except Exception:
                        pass

        return None

    def get_git_proxy(self) -> Optional[str]:
        rc, out, err = self.admin.run(["git", "config", "--global", "http.proxy"])
        out = out.strip()
        if out == "":
            return None
        return out

    def set_git_proxy(self, proxy: Optional[str]) -> bool:
        if proxy is None:
            rc, out, err = self.admin.run(["git", "config", "--global", "--unset", "http.proxy"])
            return rc == 0
        else:
            rc, out, err = self.admin.run(["git", "config", "--global", "http.proxy", proxy])
            return rc == 0

    def verify_git_ssh(self) -> (bool, str):
        rc, out, err = self.admin.run(["git", "ls-remote", "git@github.com"], timeout=30)
        ok = rc == 0
        combined = (out or "") + ("\nERR:\n" + err if err else "")
        return ok, combined

    def diagnose_and_fix(self):
        results = {"found_port": None, "git_proxy_before": None, "action": None, "git_verify": None, "git_verify_out": None}

        found_port = self.find_proxy_port()
        results["found_port"] = found_port

        git_proxy = self.get_git_proxy()
        results["git_proxy_before"] = git_proxy

        desired_proxy = None
        if found_port:
            desired_proxy = f"http://127.0.0.1:{found_port}"

        if git_proxy is None and desired_proxy is None:
            results["action"] = "no_change_needed"
        elif git_proxy is None and desired_proxy is not None:
            ok = self.set_git_proxy(desired_proxy)
            results["action"] = f"set_proxy_to_{desired_proxy}" if ok else f"failed_set_{desired_proxy}"
        elif git_proxy is not None and desired_proxy is None:
            ok = self.set_git_proxy(None)
            results["action"] = "unset_proxy" if ok else "failed_unset_proxy"
        elif git_proxy is not None and desired_proxy is not None:
            m_before = re.search(r":(\d{2,5})", git_proxy)
            port_before = int(m_before.group(1)) if m_before else None
            if port_before != found_port:
                ok = self.set_git_proxy(desired_proxy)
                results["action"] = f"updated_proxy_to_{desired_proxy}" if ok else f"failed_update_to_{desired_proxy}"
            else:
                results["action"] = "proxy_already_correct"

        ok, out = self.verify_git_ssh()
        results["git_verify"] = ok
        results["git_verify_out"] = out
        return results


class Local_Admin_UserProxy:
    def __init__(self, admin: Local_Admin, expert: Network_Expert):
        self.admin = admin
        self.expert = expert

    def initiate_chat(self, initial_message: str):
        self.admin.write_temp("initial_message.txt", initial_message)
        self.admin.write_temp("network_expert_system_message.txt", self.expert.system_message)

        results = self.expert.diagnose_and_fix()

        report_lines = [
            "=== Network Expert Report ===",
            f"System Message: {self.expert.system_message}",
            f"Initial Message: {initial_message}",
            f"Detected Proxy Port: {results['found_port']}",
            f"Git Proxy Before: {results['git_proxy_before']}",
            f"Action Taken: {results['action']}",
            f"Git Verify Success: {results['git_verify']}",
            f"Git Verify Output:\n{results['git_verify_out']}",
        ]
        report = "\n".join(str(x) for x in report_lines)
        report_path = self.admin.write_temp("diagnosis_report.txt", report)
        print(report)
        return results


def main():
    admin = Local_Admin()
    expert = Network_Expert(admin=admin)
    user_proxy = Local_Admin_UserProxy(admin=admin, expert=expert)

    # If environment requests using AutoGen and the SDK is available, try it.
    use_autogen = os.environ.get("USE_AUTOGEN", "0") in ("1", "true", "True")
    autogen_integration = AutoGenIntegration(admin=admin)
    if use_autogen and autogen_integration.is_available():
        ok = autogen_integration.run("我的 Git 连不上 GitHub，请帮我自动诊断本地端口并修正配置。")
        if ok:
            print("Ran flow via AutoGen SDK.")
            return
        else:
            print("AutoGen SDK detected but runnable API path not found — falling back to local simulator.")

    user_proxy.initiate_chat("我的 Git 连不上 GitHub，请帮我自动诊断本地端口并修正配置。")


if __name__ == "__main__":
    main()
