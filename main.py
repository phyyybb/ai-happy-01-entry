# ai-happy-01 entry: copies the bundled image to /output/entry.png (no network, deterministic).
import os
from pathlib import Path
import shutil

OUTPUT_DIR = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
src = Path(__file__).with_name("entry.png")
assert src.stat().st_size <= 1024 * 1024, "entry.png too large"
shutil.copyfile(src, OUTPUT_DIR / "entry.png")
