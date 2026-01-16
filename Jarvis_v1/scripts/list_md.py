from pathlib import Path
import sys
script = Path(__file__).resolve()
workspace_root = script.parent.parent.parent
kb = workspace_root / '20_Knowledge_Base'
if not kb.exists():
    print('KB not found:', kb)
    sys.exit(0)
mds = list(kb.rglob('*.md'))
print('Found', len(mds), '.md files under', kb)
for p in mds[:20]:
    print(p)
