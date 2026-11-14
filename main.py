# ai-happy-01 entry: copies the bundled image to /output/entry.png (no network, deterministic).
import shutil
import os
from pathlib import Path

OUTPUT_DIR = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
shutil.copyfile(Path(__file__).with_name("entry.png"), OUTPUT_DIR / "entry.png")
