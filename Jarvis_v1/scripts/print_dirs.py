from pathlib import Path
import sys
# Ensure project root in sys.path
current = Path(__file__).resolve()
project_root = current.parent.parent
workspace_root = project_root.parent
if str(workspace_root) not in sys.path:
    sys.path.append(str(workspace_root))
from Jarvis_v1.config.system_config import DIR
import json
print(json.dumps({k: str(v) for k, v in DIR.items()}, ensure_ascii=False, indent=2))
