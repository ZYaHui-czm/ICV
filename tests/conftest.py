from pathlib import Path
import sys

# 将项目根目录的 src 目录加入 sys.path，方便 pytest 收集时导入源代码
ROOT = Path(__file__).resolve().parent.parent
SRC = ROOT / "src"
sys.path.insert(0, str(SRC))
